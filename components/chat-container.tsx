"use client"

import { useState, useRef, useEffect } from "react"
import Image from "next/image"
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
    content: `Hola, soy HAL-2026, tu asistente inteligente de física.
Puedo ayudarte a resolver cualquier problema de física clásica,
siempre y cuando pertenezca a un tema dado en la materia.

Puedo explicarte conceptos complejos de forma clara. Por ejemplo, las **ecuaciones generales de movimiento rectilíneo uniforme acelerado (MRUA)**:

Posición: $$x(t) = x_0 + v_0\\, t + \\tfrac{1}{2} a t^2$$

Velocidad: $$v(t) = \\frac{dx(t)}{dt} = v_0 + a\\, t$$

Aceleración: $$a(t) = \\frac{dv(t)}{dt} = \\frac{d^2 x(t)}{dt^2} = a$$

¿Qué te gustaría aprender hoy?`,
  },
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
  }, [messages])

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
          "Hubo un error al procesar tu pregunta en el flujo pregunta -> base de datos -> contexto -> IA. Revisa la configuracion del backend.",
      }

      setMessages((prev) => [...prev, errorMessage])
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <main className="flex h-full min-h-0 flex-1 flex-col overflow-hidden">
      {/* Header */}
      <header className="flex items-center gap-3 border-b border-border bg-card/80 backdrop-blur-sm px-6 py-4">
        <div className="flex h-10 w-10 items-center justify-center rounded-xl overflow-hidden">
          <Image src="/hal2026.png" alt="HAL-2026" width={40} height={40} />
        </div>
        <div>
          <h1 className="font-semibold text-foreground">HAL-2026</h1>
          <p className="text-sm text-muted-foreground">
            Pregunte solo acerca de Fisica, o se va por la escotilla de ventilacion
          </p>
        </div>
      </header>

      {/* Messages */}
      <div ref={scrollRef} className="min-h-0 flex-1 overflow-y-auto px-4 py-6">
        <div className="mx-auto max-w-3xl space-y-6 pb-24">
          {messages.map((message) => (
            <ChatMessage key={message.id} message={message} />
          ))}
          {isLoading && (
            <div className="flex items-center gap-3">
              <div className="flex h-9 w-9 shrink-0 items-center justify-center rounded-full bg-ai-bubble border border-border">
                <Image src="/hal2026.png" alt="HAL-2026" width={20} height={20} className="animate-pulse" />
              </div>
              <div className="flex items-center gap-1 rounded-2xl rounded-bl-md bg-ai-bubble border border-border/50 px-4 py-3 shadow-sm">
                <span className="h-2 w-2 animate-bounce rounded-full bg-muted-foreground [animation-delay:-0.3s]" />
                <span className="h-2 w-2 animate-bounce rounded-full bg-muted-foreground [animation-delay:-0.15s]" />
                <span className="h-2 w-2 animate-bounce rounded-full bg-muted-foreground" />
              </div>
            </div>
          )}
        </div>
      </div>

      {/* Input */}
      <div className="sticky bottom-0 z-20 border-t border-border bg-card/90 p-4 backdrop-blur-sm">
        <div className="mx-auto max-w-3xl">
          <ChatInput onSendMessage={handleSendMessage} isLoading={isLoading} />
        </div>
      </div>
    </main>
  )
}
