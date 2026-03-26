"use client"

import { Bot, User } from "lucide-react"
import { MarkdownLatex } from "./markdown-latex"
import { cn } from "@/lib/utils"

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

  return (
    <div
      className={cn(
        "flex w-full gap-3",
        isUser ? "flex-row-reverse" : "flex-row"
      )}
    >
      {/* Avatar */}
      <div
        className={cn(
          "flex h-9 w-9 shrink-0 items-center justify-center rounded-full",
          isUser
            ? "bg-user-bubble text-user-bubble-foreground"
            : "bg-ai-bubble text-ai-bubble-foreground border border-border"
        )}
      >
        {isUser ? (
          <User className="h-4 w-4" />
        ) : (
          <Bot className="h-4 w-4" />
        )}
      </div>

      {/* Message Bubble */}
      <div
        className={cn(
          "max-w-[75%] rounded-2xl px-4 py-3 shadow-sm",
          isUser
            ? "bg-user-bubble text-user-bubble-foreground rounded-br-md"
            : "bg-ai-bubble text-ai-bubble-foreground border border-border/50 rounded-bl-md"
        )}
      >
        {isUser ? (
          <p className="leading-relaxed">{message.content}</p>
        ) : (
          <MarkdownLatex content={message.content} />
        )}
      </div>
    </div>
  )
}
