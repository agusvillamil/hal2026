"use client"

import { HalEye } from "./hal-eye"
import { MarkdownLatex } from "./markdown-latex"

interface Message {
  id: string
  role: "user" | "assistant"
  content: string
}

interface ChatMessageProps {
  message: Message
}

export function ChatMessage({ message }: ChatMessageProps) {
  const isUser = message.role === "user"

  if (isUser) {
    return (
      <div className="hal-turn hal-turn--user">
        <div className="hal-bubble hal-bubble--user">
          <div className="hal-bubble__body">
            <p>{message.content}</p>
          </div>
        </div>
      </div>
    )
  }

  return (
    <div className="hal-turn hal-turn--assistant">
      <HalEye size={34} />
      <div className="hal-bubble">
        <div className="hal-bubble__head">HAL-2026</div>
        <div className="hal-bubble__body">
          <MarkdownLatex content={message.content} />
        </div>
      </div>
    </div>
  )
}
