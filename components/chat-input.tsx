"use client"

import { useEffect, useRef, useState, type FormEvent, type KeyboardEvent } from "react"

interface ChatInputProps {
  onSendMessage: (message: string) => void
  isLoading?: boolean
}

export function ChatInput({ onSendMessage, isLoading = false }: ChatInputProps) {
  const [input, setInput] = useState("")
  const textareaRef = useRef<HTMLTextAreaElement>(null)

  useEffect(() => {
    const textarea = textareaRef.current
    if (!textarea) return

    textarea.style.height = "auto"
    textarea.style.height = input ? `${Math.min(textarea.scrollHeight, 200)}px` : ""
  }, [input])

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
        ref={textareaRef}
        className="hal-textarea"
        value={input}
        onChange={(e) => setInput(e.target.value)}
        onKeyDown={handleKeyDown}
        placeholder="Escribí tu pregunta sobre Física I..."
        disabled={isLoading}
        rows={1}
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
