import { ChatContainer } from "@/components/chat-container"
import { PhysicsBackground } from "@/components/physics-background"

export default function Index() {
  return (
    <div className="relative flex h-screen w-full overflow-hidden bg-background">
      <PhysicsBackground />
      <ChatContainer />
    </div>
  )
}
