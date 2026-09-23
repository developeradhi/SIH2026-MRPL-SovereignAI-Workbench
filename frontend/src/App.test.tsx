import { fireEvent, render, waitFor } from '@testing-library/react'
import { vi } from 'vitest'

import App from './App'

const ok = (body: unknown) => new Response(JSON.stringify(body), { status: 200 })

describe('App', () => {
  beforeEach(() => {
    vi.stubGlobal('fetch', vi.fn(async (url: string) => {
      if (url.endsWith('/health')) {
        return ok({ status: 'ok', service: 'backend' })
      }
      if (url.endsWith('/security/network-status')) {
        return ok({
          offline_mode: true,
          model_endpoint: 'http://127.0.0.1:11434',
          model_endpoint_local: true,
          model_endpoint_reachable: false,
          note: 'placeholder'
        })
      }
      if (url.endsWith('/tasks')) {
        return ok([])
      }
      return new Response('{}', { status: 404 })
    }) as typeof fetch)
  })

  it('renders dashboard heading', async () => {
    const { findByText } = render(<App />)
    expect(await findByText(/SovereignAI Workbench Dashboard/i)).toBeInTheDocument()
  })

  it('sends uploaded document id and refreshes task status', async () => {
    const fetchMock = vi.fn(async (url: string, init?: RequestInit) => {
      if (url.endsWith('/health')) return ok({ status: 'ok', service: 'backend' })
      if (url.endsWith('/security/network-status')) {
        return ok({
          offline_mode: true,
          model_endpoint: 'http://127.0.0.1:11434',
          model_endpoint_local: true,
          model_endpoint_reachable: false,
          note: 'placeholder'
        })
      }
      if (url.endsWith('/documents/upload')) {
        return ok({
          document_id: 'doc-1',
          filename: 'evidence.txt',
          extension: '.txt',
          size_bytes: 12,
          checksum_sha256: 'abc',
          stored_path: '/tmp/evidence.txt'
        })
      }
      if (url.endsWith('/tasks') && init?.method === 'POST') {
        const payload = JSON.parse(String(init.body))
        expect(payload.document_ids).toEqual(['doc-1'])
        return ok({
          task_id: 'task-1',
          title: payload.title,
          prompt: payload.prompt,
          status: 'created',
          document_ids: payload.document_ids,
          requires_review: payload.requires_review,
          output_files: [],
          created_at: '2026-01-01T00:00:00Z',
          updated_at: '2026-01-01T00:00:00Z',
          events: []
        })
      }
      if (url.endsWith('/tasks/task-1')) {
        return ok({
          task_id: 'task-1',
          title: 'Inspection report summary',
          prompt: 'Analyze findings and prepare output package',
          status: 'completed',
          document_ids: ['doc-1'],
          requires_review: true,
          output_files: ['task-1_result.json'],
          created_at: '2026-01-01T00:00:00Z',
          updated_at: '2026-01-01T00:00:01Z',
          events: []
        })
      }
      if (url.endsWith('/tasks')) return ok([])
      return new Response('{}', { status: 404 })
    })
    vi.stubGlobal('fetch', fetchMock as typeof fetch)

    const { container, getByText } = render(<App />)
    await waitFor(() => expect(fetchMock).toHaveBeenCalledWith(expect.stringContaining('/health'), undefined))

    const file = new File(['hello'], 'evidence.txt', { type: 'text/plain' })
    const fileInput = container.querySelector('input[name="document"]') as HTMLInputElement
    fireEvent.change(fileInput, { target: { files: [file] } })
    fireEvent.click(getByText('Upload'))

    await waitFor(() => expect(fetchMock).toHaveBeenCalledWith(expect.stringContaining('/documents/upload'), expect.any(Object)))

    fireEvent.click(getByText('Create Task'))

    await waitFor(() => expect(fetchMock).toHaveBeenCalledWith(expect.stringContaining('/tasks/task-1'), undefined))
    await waitFor(() => expect(getByText(/task-1_result.json/i)).toBeInTheDocument())
  })
})
