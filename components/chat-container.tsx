"use client"

import { useState, useRef, useEffect } from "react"
import { ChatMessage } from "./chat-message"
import { ChatInput } from "./chat-input"
import { ScrollArea } from "@/components/ui/scroll-area"
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
    content: `¡Hola! Soy tu tutor de física con IA. Puedo ayudarte con cualquier tema de física, desde mecánica clásica hasta física cuántica.

Puedo explicarte conceptos complejos y mostrarte las ecuaciones matemáticas de forma clara. Por ejemplo, las **ecuaciones de Maxwell** que describen el electromagnetismo:

$$\\nabla \\cdot \\mathbf{E} = \\frac{\\rho}{\\varepsilon_0}$$

$$\\nabla \\cdot \\mathbf{B} = 0$$

$$\\nabla \\times \\mathbf{E} = -\\frac{\\partial \\mathbf{B}}{\\partial t}$$

$$\\nabla \\times \\mathbf{B} = \\mu_0\\mathbf{J} + \\mu_0\\varepsilon_0\\frac{\\partial \\mathbf{E}}{\\partial t}$$

¿Sobre qué tema de física te gustaría aprender hoy?`,
  },
]

const assistantResponses: Record<string, string> = {
  default: `Excelente pregunta. Déjame explicarte este concepto de física.

La **ecuación de Schrödinger** es fundamental en mecánica cuántica y describe cómo evoluciona el estado cuántico de un sistema físico con el tiempo:

$$i\\hbar\\frac{\\partial}{\\partial t}\\Psi(\\mathbf{r},t) = \\hat{H}\\Psi(\\mathbf{r},t)$$

Donde:
- $\\Psi$ es la función de onda
- $\\hbar$ es la constante de Planck reducida
- $\\hat{H}$ es el operador Hamiltoniano

Para una partícula libre, el Hamiltoniano toma la forma:

$$\\hat{H} = -\\frac{\\hbar^2}{2m}\\nabla^2 + V(\\mathbf{r})$$

¿Te gustaría que profundice en algún aspecto específico de esta ecuación?`,
  energia: `La **energía** es una de las cantidades más fundamentales en física. La famosa ecuación de Einstein relaciona masa y energía:

$$E = mc^2$$

En mecánica clásica, la energía total de un sistema es la suma de la energía cinética y potencial:

$$E_{total} = E_c + E_p = \\frac{1}{2}mv^2 + mgh$$

El **principio de conservación de la energía** establece que en un sistema aislado, la energía total permanece constante:

$$\\frac{dE}{dt} = 0$$

¿Quieres que exploremos algún tipo específico de energía o sus aplicaciones?`,
  ondas: `Las **ondas** son perturbaciones que transportan energía sin transportar materia. La ecuación de onda general es:

$$\\frac{\\partial^2 u}{\\partial t^2} = v^2 \\frac{\\partial^2 u}{\\partial x^2}$$

Para una onda armónica, la solución tiene la forma:

$$u(x,t) = A\\sin(kx - \\omega t + \\phi)$$

Donde:
- $A$ es la amplitud
- $k = \\frac{2\\pi}{\\lambda}$ es el número de onda
- $\\omega = 2\\pi f$ es la frecuencia angular
- $\\phi$ es la fase inicial

La **relación de dispersión** conecta $\\omega$ y $k$:

$$\\omega = vk$$

¿Te interesa aprender sobre ondas electromagnéticas, ondas sonoras o algún otro tipo?`,
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

    // Simulate AI response
    await new Promise((resolve) => setTimeout(resolve, 1500))

    const lowerContent = content.toLowerCase()
    let responseKey = "default"
    if (lowerContent.includes("energía") || lowerContent.includes("energia")) {
      responseKey = "energia"
    } else if (lowerContent.includes("onda") || lowerContent.includes("wave")) {
      responseKey = "ondas"
    }

    const assistantMessage: Message = {
      id: (Date.now() + 1).toString(),
      role: "assistant",
      content: assistantResponses[responseKey],
    }

    setMessages((prev) => [...prev, assistantMessage])
    setIsLoading(false)
  }

  return (
    <main className="flex flex-1 flex-col h-full overflow-hidden">
      {/* Header */}
      <header className="flex items-center gap-3 border-b border-border bg-card/80 backdrop-blur-sm px-6 py-4">
        <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-primary/10">
          <Atom className="h-5 w-5 text-primary" />
        </div>
        <div>
          <h1 className="font-semibold text-foreground">Tutoría de Física</h1>
          <p className="text-sm text-muted-foreground">
            Aprende física con explicaciones claras y fórmulas en LaTeX
          </p>
        </div>
      </header>

      {/* Messages */}
      <ScrollArea className="flex-1 px-4 py-6" ref={scrollRef}>
        <div className="mx-auto max-w-3xl space-y-6">
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
      </ScrollArea>

      {/* Input */}
      <div className="border-t border-border bg-card/80 backdrop-blur-sm p-4">
        <div className="mx-auto max-w-3xl">
          <ChatInput onSendMessage={handleSendMessage} isLoading={isLoading} />
        </div>
      </div>
    </main>
  )
}
