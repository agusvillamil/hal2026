"use client"

import { useState, type FormEvent, type KeyboardEvent } from "react"
import { ArrowUp } from "lucide-react"
import { Button } from "@/components/ui/button"
import { cn } from "@/lib/utils"

interface ChatInputProps {
  onSendMessage: (message: string) => void
  isLoading?: boolean
}

export function ChatInput({ onSendMessage, isLoading = false }: ChatInputProps) {
  const [input, setInput] = useState("")

  const handleSubmit = (e: FormEvent) => {
    e.preventDefault()
    if (input.trim() && !isLoading) {
      onSendMessage(input.trim())
      setInput("")
    }
  }

  const handleKeyDown = (e: KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault()
      handleSubmit(e)
    }
  }

  return (
    <form onSubmit={handleSubmit} className="w-full">
      <div className="relative flex items-end gap-2 rounded-2xl border border-border bg-card p-2 shadow-lg transition-shadow focus-within:shadow-xl focus-within:ring-2 focus-within:ring-accent/20">
        <textarea
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="Hacer una pregunta sobre física..."
          disabled={isLoading}
          rows={1}
          className={cn(
            "max-h-32 min-h-[44px] flex-1 resize-none bg-transparent px-3 py-2.5 text-foreground placeholder:text-muted-foreground focus:outline-none disabled:opacity-50",
            "scrollbar-thin scrollbar-thumb-border scrollbar-track-transparent"
          )}
          style={{
            height: "auto",
            minHeight: "44px",
          }}
          onInput={(e) => {
            const target = e.target as HTMLTextAreaElement
            target.style.height = "auto"
            target.style.height = `${Math.min(target.scrollHeight, 128)}px`
          }}
        />
        <Button
          type="submit"
          size="icon"
          disabled={!input.trim() || isLoading}
          className={cn(
            "h-10 w-10 shrink-0 rounded-xl bg-primary text-primary-foreground transition-all hover:bg-primary/90",
            "disabled:bg-muted disabled:text-muted-foreground"
          )}
        >
          <ArrowUp className="h-5 w-5" />
          <span className="sr-only">Enviar mensaje</span>
        </Button>
      </div>
      <p className="mt-2 text-center text-xs text-muted-foreground">
        HAL-2026 puede cometer errores. Verifica siempre la información importante.
      </p>
    </form>
  )
}
