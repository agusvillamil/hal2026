import Image from "next/image"
import type { CSSProperties } from "react"

interface HalEyeProps {
  size?: number
  breathing?: boolean
}

/**
 * The HAL-2026 brand mark / avatar: the real logo (public/hal2026.png — a
 * glossy blue iris in a polished chrome bezel) shown in a circular frame lit
 * by the design system's soft blue glow, with a gentle breathing animation.
 */
export function HalEye({ size = 48, breathing = true }: HalEyeProps) {
  const wrap: CSSProperties = {
    width: size,
    height: size,
    borderRadius: "50%",
    overflow: "hidden",
    position: "relative",
    flex: `0 0 ${size}px`,
    boxShadow: size >= 40 ? "var(--eye-shadow)" : "var(--eye-shadow-sm)",
    animation: breathing ? "hal-breathe 3.6s ease-in-out infinite" : "none",
  }

  return (
    <div className="hal-eye" style={wrap} aria-hidden="true">
      <Image
        src="/hal2026.png"
        alt="HAL-2026"
        width={size}
        height={size}
        priority={size >= 40}
        style={{
          width: "100%",
          height: "100%",
          objectFit: "cover",
          // slight bleed so the bezel reaches the circular edge cleanly
          transform: "scale(1.04)",
        }}
      />
    </div>
  )
}
