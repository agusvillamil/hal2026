"use client"

export function PhysicsBackground() {
  return (
    <div className="pointer-events-none fixed inset-0 overflow-hidden opacity-[0.04]">
      <svg
        className="absolute inset-0 h-full w-full"
        xmlns="http://www.w3.org/2000/svg"
      >
        <defs>
          <pattern
            id="physics-pattern"
            x="0"
            y="0"
            width="400"
            height="400"
            patternUnits="userSpaceOnUse"
          >
            {/* Elliptical orbit 1 */}
            <ellipse
              cx="200"
              cy="200"
              rx="150"
              ry="80"
              fill="none"
              stroke="currentColor"
              strokeWidth="1"
              className="text-primary"
            />
            {/* Elliptical orbit 2 - tilted */}
            <ellipse
              cx="200"
              cy="200"
              rx="120"
              ry="60"
              fill="none"
              stroke="currentColor"
              strokeWidth="0.8"
              className="text-primary"
              transform="rotate(45 200 200)"
            />
            {/* Elliptical orbit 3 - tilted other way */}
            <ellipse
              cx="200"
              cy="200"
              rx="100"
              ry="40"
              fill="none"
              stroke="currentColor"
              strokeWidth="0.6"
              className="text-primary"
              transform="rotate(-30 200 200)"
            />
            {/* Nucleus */}
            <circle
              cx="200"
              cy="200"
              r="8"
              fill="currentColor"
              className="text-primary"
            />
            {/* Electron particles on orbits */}
            <circle
              cx="350"
              cy="200"
              r="4"
              fill="currentColor"
              className="text-accent"
            />
            <circle
              cx="285"
              cy="115"
              r="3"
              fill="currentColor"
              className="text-accent"
            />
            <circle
              cx="115"
              cy="240"
              r="3.5"
              fill="currentColor"
              className="text-accent"
            />
          </pattern>
          
          <pattern
            id="trajectory-pattern"
            x="0"
            y="0"
            width="600"
            height="600"
            patternUnits="userSpaceOnUse"
          >
            {/* Parabolic trajectory */}
            <path
              d="M 50 500 Q 200 100 350 500"
              fill="none"
              stroke="currentColor"
              strokeWidth="1"
              strokeDasharray="8 4"
              className="text-primary"
            />
            {/* Wave pattern */}
            <path
              d="M 400 300 C 430 250 470 250 500 300 C 530 350 570 350 600 300"
              fill="none"
              stroke="currentColor"
              strokeWidth="1"
              className="text-primary"
            />
            {/* Vector arrows */}
            <line
              x1="100"
              y1="400"
              x2="200"
              y2="350"
              stroke="currentColor"
              strokeWidth="1.5"
              className="text-primary"
            />
            <polygon
              points="200,350 190,355 192,345"
              fill="currentColor"
              className="text-primary"
            />
            {/* Small dots representing particles */}
            <circle cx="450" cy="150" r="2" fill="currentColor" className="text-accent" />
            <circle cx="480" cy="180" r="2" fill="currentColor" className="text-accent" />
            <circle cx="510" cy="160" r="2" fill="currentColor" className="text-accent" />
          </pattern>
        </defs>
        
        <rect width="100%" height="100%" fill="url(#physics-pattern)" />
        <rect width="100%" height="100%" fill="url(#trajectory-pattern)" style={{ transform: 'translate(200px, 100px)' }} />
      </svg>
    </div>
  )
}
