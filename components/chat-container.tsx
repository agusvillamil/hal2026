"use client"

import { useState, useRef, useEffect } from "react"
import { ChatMessage } from "./chat-message"
import { ChatInput } from "./chat-input"
import { Atom } from "lucide-react"

interface Message {
  id: string
  role: "user" | "assistant"
  content: string
}

const initialMessages: Message[] = [
  {
    id: "1",
    role: "assistant",
    content: `Hola, Soy HAL-2026, tu asistente de física. Puedo ayudarte con cualquier tema de física, mientras que pertenezca a los temas dados en la materia Fisica I.

Puedo explicarte conceptos complejos y mostrarte las ecuaciones matemáticas de forma clara. Por ejemplo, las **ecuaciones de Maxwell** que describen el electromagnetismo:

$$\\nabla \\cdot \\mathbf{E} = \\frac{\\rho}{\\varepsilon_0}$$

$$\\nabla \\cdot \\mathbf{B} = 0$$

$$\\nabla \\times \\mathbf{E} = -\\frac{\\partial \\mathbf{B}}{\\partial t}$$

$$\\nabla \\times \\mathbf{B} = \\mu_0\\mathbf{J} + \\mu_0\\varepsilon_0\\frac{\\partial \\mathbf{E}}{\\partial t}$$

¿Sobre qué tema de física te gustaría aprender hoy?`,
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
  _question: SavedQuestion,
  context: RetrievedContext[]
): Promise<string> {
  // TODO: Integrar proveedor/modelo de IA cuando se defina.
  if (context.length === 0) {
    return "Recibi tu pregunta y la guarde correctamente. Aun no hay base de contexto ni proveedor de IA configurados para generar una respuesta final."
  }

  return "Recibi tu pregunta, encontre contexto en la base y quedo lista para enviarse al modelo de IA elegido."
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
        <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-primary/10">
          <Atom className="h-5 w-5 text-primary" />
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
                <Atom className="h-4 w-4 text-ai-bubble-foreground animate-pulse" />
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
