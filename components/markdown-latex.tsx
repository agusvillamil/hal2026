"use client"

import ReactMarkdown from "react-markdown"
import remarkMath from "remark-math"
import rehypeKatex from "rehype-katex"
import "katex/dist/katex.min.css"

interface MarkdownLatexProps {
  content: string
  className?: string
}

export function MarkdownLatex({ content, className = "" }: MarkdownLatexProps) {
  return (
    <div className={`markdown-content ${className}`}>
      <ReactMarkdown
        remarkPlugins={[remarkMath]}
        rehypePlugins={[rehypeKatex]}
        components={{
          p: ({ children }) => (
            <p className="mb-3 last:mb-0 leading-relaxed">{children}</p>
          ),
          h1: ({ children }) => (
            <h1 className="mb-4 text-xl font-semibold">{children}</h1>
          ),
          h2: ({ children }) => (
            <h2 className="mb-3 text-lg font-semibold">{children}</h2>
          ),
          h3: ({ children }) => (
            <h3 className="mb-2 text-base font-semibold">{children}</h3>
          ),
          ul: ({ children }) => (
            <ul className="mb-3 list-disc pl-5 space-y-1">{children}</ul>
          ),
          ol: ({ children }) => (
            <ol className="mb-3 list-decimal pl-5 space-y-1">{children}</ol>
          ),
          li: ({ children }) => (
            <li className="leading-relaxed">{children}</li>
          ),
          code: ({ children, className }) => {
            const isInline = !className
            return isInline ? (
              <code className="rounded bg-muted px-1.5 py-0.5 font-mono text-sm">
                {children}
              </code>
            ) : (
              <code className="block overflow-x-auto rounded-lg bg-muted p-4 font-mono text-sm">
                {children}
              </code>
            )
          },
          pre: ({ children }) => (
            <pre className="mb-3 overflow-x-auto rounded-lg bg-muted p-4">
              {children}
            </pre>
          ),
          blockquote: ({ children }) => (
            <blockquote className="mb-3 border-l-4 border-accent pl-4 italic text-muted-foreground">
              {children}
            </blockquote>
          ),
          strong: ({ children }) => (
            <strong className="font-semibold">{children}</strong>
          ),
          em: ({ children }) => <em className="italic">{children}</em>,
        }}
      >
        {content}
      </ReactMarkdown>
    </div>
  )
}
