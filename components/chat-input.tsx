"use client"

import { useState, type FormEvent, type KeyboardEvent } from "react"

interface ChatInputProps {
  onSendMessage: (message: string) => void
  isLoading?: boolean
}

export function ChatInput({ onSendMessage, isLoading = false }: ChatInputProps) {
  const [input, setInput] = useState("")

  const handleSubmit = (e?: FormEvent) => {
    e?.preventDefault()
    if (input.trim() && !isLoading) {
      onSendMessage(input.trim())
      setInput("")
    }
  }

  const handleKeyDown = (e: KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault()
      handleSubmit()
    }
  }

  return (
    <div className="hal-composer">
      <textarea
        className="hal-textarea"
        value={input}
        onChange={(e) => setInput(e.target.value)}
        onKeyDown={handleKeyDown}
        placeholder="Escribí tu pregunta sobre Física I..."
        disabled={isLoading}
        rows={1}
        onInput={(e) => {
          const target = e.target as HTMLTextAreaElement
          target.style.height = "auto"
          target.style.height = `${Math.min(target.scrollHeight, 200)}px`
        }}
      />
      <button
        type="button"
        className="hal-send"
        onClick={() => handleSubmit()}
        disabled={!input.trim() || isLoading}
      >
        Enviar
      </button>
    </div>
  )
}
