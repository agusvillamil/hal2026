"use client"

import { useState, useRef, useEffect } from "react"
import { HalEye } from "./hal-eye"
import { ChatMessage } from "./chat-message"
import { ChatInput } from "./chat-input"

interface Message {
  id: string
  role: "user" | "assistant"
  content: string
}

const initialMessages: Message[] = [
  {
    id: "1",
    role: "assistant",
    content: `¡Hola! Soy HAL-2026, tu asistente de Física I. Contame qué tema estás viendo y lo resolvemos juntos, conceptos, ecuaciones y demostraciones.

Por ejemplo, las ecuaciones generales del movimiento rectilíneo uniformemente acelerado (MRUA):

Posición: $$x(t) = x_0 + v_0\\, t + \\tfrac{1}{2} a t^2$$

Velocidad: $$v(t) = \\frac{dx(t)}{dt} = v_0 + a\\, t$$

Aceleración: $$a(t) = \\frac{dv(t)}{dt} = \\frac{d^2 x(t)}{dt^2} = a$$

¿Qué te gustaría aprender hoy?`,
  },
]

const DEFAULT_SUGGESTIONS = [
  "¿Qué es el campo eléctrico?",
  "Ley de Newton aplicada",
  "Movimiento armónico simple",
  "Primera ley de la termodinámica",
]

interface SavedQuestion {
  id: string
  text: string
  createdAt: string
}

interface RetrievedContext {
  source: string
  content: string
}

async function saveQuestionToDatabase(question: string): Promise<SavedQuestion> {
  // TODO: Reemplazar por insercion real en base de datos.
  return {
    id: crypto.randomUUID(),
    text: question,
    createdAt: new Date().toISOString(),
  }
}

async function searchContextInDatabase(_savedQuestion: SavedQuestion): Promise<RetrievedContext[]> {
  // TODO: Reemplazar por busqueda semantica/contextual en base de datos.
  return []
}

async function generateAnswerWithAI(
  question: SavedQuestion,
  _context: RetrievedContext[]
): Promise<string> {
  const apiUrl = process.env.NEXT_PUBLIC_API_URL
  if (!apiUrl) throw new Error("NEXT_PUBLIC_API_URL no está configurada en .env")

  const res = await fetch(`${apiUrl}/chat`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "ngrok-skip-browser-warning": "true",
    },
    body: JSON.stringify({ mensaje: question.text }),
  })

  if (!res.ok) throw new Error(`Error del servidor: ${res.status}`)

  const data = await res.json()
  return data.respuesta
}

async function runQuestionPipeline(questionText: string): Promise<string> {
  const savedQuestion = await saveQuestionToDatabase(questionText)
  const context = await searchContextInDatabase(savedQuestion)
  return generateAnswerWithAI(savedQuestion, context)
}

export function ChatContainer() {
  const [messages, setMessages] = useState<Message[]>(initialMessages)
  const [isLoading, setIsLoading] = useState(false)
  const scrollRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    if (scrollRef.current) {
      scrollRef.current.scrollTop = scrollRef.current.scrollHeight
    }
  }, [messages, isLoading])

  const handleSendMessage = async (content: string) => {
    const userMessage: Message = {
      id: Date.now().toString(),
      role: "user",
      content,
    }

    setMessages((prev) => [...prev, userMessage])
    setIsLoading(true)

    try {
      const answer = await runQuestionPipeline(content)

      const assistantMessage: Message = {
        id: (Date.now() + 1).toString(),
        role: "assistant",
        content: answer,
      }

      setMessages((prev) => [...prev, assistantMessage])
    } catch {
      const errorMessage: Message = {
        id: (Date.now() + 1).toString(),
        role: "assistant",
        content:
          "Uy, hubo un error al procesar tu pregunta en el flujo pregunta → base de datos → contexto → IA. Revisá la configuración del backend.",
      }

      setMessages((prev) => [...prev, errorMessage])
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <div className="hal-app">
      {/* Header */}
      <header className="hal-header">
        <HalEye size={48} />
        <div className="hal-header__meta">
          <div className="hal-title">HAL-2026</div>
          <div className="hal-tagline">
            Tu asistente de Física I. Preguntame acerca de física o te vas por la escotilla de ventilación.
          </div>
        </div>
        <div className="hal-hud-block">
          <div className={isLoading ? "" : "hud-online"}>
            <span
              style={{
                display: "inline-block",
                width: 5,
                height: 5,
                borderRadius: "50%",
                background: isLoading ? "var(--halo-flare)" : "var(--halo)",
                boxShadow: `0 0 6px ${isLoading ? "var(--halo-flare)" : "var(--halo)"}`,
                marginRight: 8,
                verticalAlign: "middle",
                animation: isLoading
                  ? "hal-pulse 1.2s ease-in-out infinite"
                  : "hal-pulse 2.4s ease-in-out infinite",
              }}
            />
            {isLoading ? "Pensando…" : "En línea"}
          </div>
          <div>Física I · UNS</div>
          <div>Modo RAG</div>
        </div>
      </header>

      {/* Stream */}
      <div ref={scrollRef} className="hal-stream">
        <div className="hal-stream__inner">
          {messages.map((message) => (
            <ChatMessage key={message.id} message={message} />
          ))}
          {isLoading && (
            <div className="hal-turn hal-turn--assistant">
              <HalEye size={34} />
              <div className="hal-bubble">
                <div className="hal-bubble__head">HAL-2026 · pensando</div>
                <div className="hal-bubble__body hal-thinking">
                  <span />
                  <span />
                  <span />
                </div>
              </div>
            </div>
          )}
        </div>
      </div>

      {/* Footer */}
      <footer className="hal-footer">
        <div className="hal-chips">
          {DEFAULT_SUGGESTIONS.map((s) => (
            <button
              key={s}
              type="button"
              className="hal-chip"
              onClick={() => handleSendMessage(s)}
              disabled={isLoading}
            >
              {s}
            </button>
          ))}
        </div>
        <ChatInput onSendMessage={handleSendMessage} isLoading={isLoading} />
        <div className="hal-disclaimer">
          HAL-2026 puede cometer errores. Verificá siempre la información importante.
        </div>
      </footer>
    </div>
  )
}
