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

type ChatHistoryMessage = Pick<Message, "role" | "content">

const MAX_HISTORY_MESSAGES = 6
const MAX_HISTORY_MESSAGE_CHARS = 1200

const initialMessages: Message[] = [
  {
    id: "1",
    role: "assistant",
    content: 
`¡Hola! Soy HAL-2026, tu asistente inteligente de Física I. 
Puedo ayudarte a resolver cualquier problema de física clásica, 
siempre y cuando pertenezca a un tema dado en la materia.

Puedo explicarte conceptos complejos de forma clara. 
Por ejemplo, las ecuaciones generales 
del movimiento rectilíneo uniformemente acelerado (MRUA):

Posición: $$x(t) = x_0 + v_0\\, t + \\tfrac{1}{2} a t^2$$

Velocidad: $$v(t) = \\frac{dx(t)}{dt} = v_0 + a\\, t$$

Aceleración: $$a(t) = \\frac{dv(t)}{dt} = \\frac{d^2 x(t)}{dt^2} = a$$

¿Qué te gustaría aprender hoy?`,
  },
]

const DEFAULT_SUGGESTIONS = [
  "¿Puede una partícula tener aceleración si se mueve a una rapidez constante?",
  "Ley de Newton aplicada",
  "Movimiento armónico simple",
  "¿Qué papel juega la inercia cuando se aplica una fuerza sobre un cuerpo para alterar su movimiento?",
]

function truncateHistoryContent(content: string): string {
  if (content.length <= MAX_HISTORY_MESSAGE_CHARS) return content
  return `${content.slice(0, MAX_HISTORY_MESSAGE_CHARS).trim()}...`
}

function buildChatHistory(messages: Message[]): ChatHistoryMessage[] {
  return messages
    .filter((message) => message.id !== initialMessages[0].id)
    .slice(-MAX_HISTORY_MESSAGES)
    .map((message) => ({
      role: message.role,
      content: truncateHistoryContent(message.content),
    }))
}

async function fetchAnswer(question: string, history: ChatHistoryMessage[]): Promise<string> {
  const apiUrl = process.env.NEXT_PUBLIC_API_URL
  if (!apiUrl) throw new Error("NEXT_PUBLIC_API_URL no está configurada en .env")

  // El backend hace el flujo completo de RAG: búsqueda de contexto + generación.
  const res = await fetch(`${apiUrl}/chat`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "ngrok-skip-browser-warning": "true",
    },
    body: JSON.stringify({ mensaje: question, historial: history }),
  })

  if (!res.ok) throw new Error(`Error del servidor: ${res.status}`)

  const data = await res.json()
  return data.respuesta
}

export function ChatContainer() {
  const [messages, setMessages] = useState<Message[]>(initialMessages)
  const [isLoading, setIsLoading] = useState(false)
  const scrollRef = useRef<HTMLDivElement>(null)
  const showSuggestions = !messages.some((message) => message.role === "user")

  useEffect(() => {
    if (scrollRef.current) {
      scrollRef.current.scrollTop = scrollRef.current.scrollHeight
    }
  }, [messages, isLoading])

  const handleSendMessage = async (content: string) => {
    const history = buildChatHistory(messages)
    const userMessage: Message = {
      id: Date.now().toString(),
      role: "user",
      content,
    }

    setMessages((prev) => [...prev, userMessage])
    setIsLoading(true)

    try {
      const answer = await fetchAnswer(content, history)

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
            Tu asistente inteligente de Física I. Pregunte solo acerca de física, o se va por la escotilla de ventilación.
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
        {showSuggestions && (
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
        )}
        <ChatInput onSendMessage={handleSendMessage} isLoading={isLoading} />
        <div className="hal-disclaimer">
          HAL-2026 puede cometer errores. Verificá siempre la información importante.
        </div>
      </footer>
    </div>
  )
}
