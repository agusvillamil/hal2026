"use client"

// Renderizador de diagramas de cuerpo libre (DCL).
//
// El LLM solo decide la física (qué fuerzas hay y hacia dónde apuntan) y la
// entrega como JSON. Toda la geometría vive acá, así el dibujo siempre sale
// limpio y consistente. El SVG se arma desde valores ya parseados: el modelo
// nunca inyecta marcado, por lo que no hace falta sanitizar.

// ── Tipos ────────────────────────────────────────────────────────────────────

export interface FbdForce {
  etiqueta: string
  /** Grados, convención matemática: 0 = derecha, 90 = arriba. */
  angulo: number
  color?: string
}

export interface FbdSpec {
  objeto: string
  /** Grados del plano de apoyo (0 = horizontal). */
  inclinacion: number
  fuerzas: FbdForce[]
}

// ── Parseo ───────────────────────────────────────────────────────────────────

function aFuerza(valor: unknown): FbdForce | null {
  if (!valor || typeof valor !== "object") return null
  const f = valor as Record<string, unknown>
  const angulo = Number(f.angulo)
  if (typeof f.etiqueta !== "string" || !Number.isFinite(angulo)) return null
  return {
    etiqueta: f.etiqueta,
    angulo,
    color: typeof f.color === "string" ? f.color : undefined,
  }
}

/** Convierte un bloque ```fbd crudo en un spec, o null si no es válido. */
export function parseFbdSpec(raw: string): FbdSpec | null {
  let data: unknown
  try {
    data = JSON.parse(raw)
  } catch {
    return null
  }
  if (!data || typeof data !== "object") return null

  const obj = data as Record<string, unknown>
  if (!Array.isArray(obj.fuerzas)) return null

  const fuerzas = obj.fuerzas
    .map(aFuerza)
    .filter((f): f is FbdForce => f !== null)
  if (fuerzas.length === 0) return null

  const inclinacion = Number(obj.inclinacion)
  return {
    objeto: typeof obj.objeto === "string" ? obj.objeto : "",
    inclinacion: Number.isFinite(inclinacion) ? inclinacion : 0,
    fuerzas,
  }
}

// ── Geometría ──────────────────────────────────────────────────────────────────

const LIENZO = { ancho: 260, alto: 220 }
const CENTRO = { x: LIENZO.ancho / 2, y: LIENZO.alto / 2 }
const CUERPO = { ancho: 76, alto: 52 }
const LARGO_FLECHA = 66
const SEPARACION_ETIQUETA = 16
const MEDIA_BASE = 96

/** Punto polar (grados, convención matemática) → coordenada SVG (y crece hacia abajo). */
function polar(x: number, y: number, grados: number, radio: number) {
  const rad = (grados * Math.PI) / 180
  return { x: x + Math.cos(rad) * radio, y: y - Math.sin(rad) * radio }
}

// ── Subcomponentes ─────────────────────────────────────────────────────────────

function PuntaFlecha() {
  return (
    <marker
      id="fbd-arrow"
      viewBox="0 0 10 10"
      refX={8}
      refY={5}
      markerWidth={7}
      markerHeight={7}
      orient="auto-start-reverse"
    >
      <path d="M0,0 L10,5 L0,10 z" fill="context-stroke" />
    </marker>
  )
}

function Fuerza({ fuerza }: { fuerza: FbdForce }) {
  const punta = polar(CENTRO.x, CENTRO.y, fuerza.angulo, LARGO_FLECHA)
  const etiqueta = polar(CENTRO.x, CENTRO.y, fuerza.angulo, LARGO_FLECHA + SEPARACION_ETIQUETA)
  const color = fuerza.color ?? "var(--halo-flare)"
  return (
    <g>
      <line
        x1={CENTRO.x}
        y1={CENTRO.y}
        x2={punta.x}
        y2={punta.y}
        stroke={color}
        strokeWidth={2.5}
        markerEnd="url(#fbd-arrow)"
      />
      <text
        x={etiqueta.x}
        y={etiqueta.y}
        fill="var(--foreground)"
        fontSize={15}
        fontStyle="italic"
        textAnchor="middle"
        dominantBaseline="middle"
      >
        {fuerza.etiqueta}
      </text>
    </g>
  )
}

/** Cuerpo apoyado sobre su superficie. Se rota todo el grupo según la inclinación;
 *  las fuerzas se dibujan aparte en ángulos absolutos. */
function CuerpoApoyado({ objeto, inclinacion }: { objeto: string; inclinacion: number }) {
  const baseY = CENTRO.y + CUERPO.alto / 2
  const ticks = Array.from({ length: 9 }, (_, i) => {
    const x = CENTRO.x - MEDIA_BASE + (i * (2 * MEDIA_BASE)) / 8
    return <line key={i} x1={x} y1={baseY} x2={x - 7} y2={baseY + 7} stroke="var(--border)" strokeWidth={1} />
  })

  return (
    <g transform={`rotate(${-inclinacion} ${CENTRO.x} ${CENTRO.y})`}>
      <line x1={CENTRO.x - MEDIA_BASE} y1={baseY} x2={CENTRO.x + MEDIA_BASE} y2={baseY} stroke="var(--border)" strokeWidth={2} />
      {ticks}
      <rect
        x={CENTRO.x - CUERPO.ancho / 2}
        y={CENTRO.y - CUERPO.alto / 2}
        width={CUERPO.ancho}
        height={CUERPO.alto}
        rx={4}
        fill="var(--halo)"
        fillOpacity={0.18}
        stroke="var(--halo)"
        strokeWidth={1.5}
      />
      {objeto && (
        <text x={CENTRO.x} y={CENTRO.y} fill="var(--foreground)" fontSize={13} textAnchor="middle" dominantBaseline="middle">
          {objeto}
        </text>
      )}
    </g>
  )
}

// ── Componente principal ────────────────────────────────────────────────────────

export function FreeBodyDiagram({ spec }: { spec: FbdSpec }) {
  return (
    <div style={{ display: "flex", justifyContent: "center", margin: "12px 0" }}>
      <svg
        viewBox={`0 0 ${LIENZO.ancho} ${LIENZO.alto}`}
        width="100%"
        style={{ maxWidth: 320 }}
        role="img"
        aria-label={`Diagrama de cuerpo libre de ${spec.objeto || "el cuerpo"}`}
      >
        <defs>
          <PuntaFlecha />
        </defs>
        <CuerpoApoyado objeto={spec.objeto} inclinacion={spec.inclinacion} />
        {spec.fuerzas.map((fuerza, i) => (
          <Fuerza key={i} fuerza={fuerza} />
        ))}
      </svg>
    </div>
  )
}
