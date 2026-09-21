
import { useEffect, useRef } from "react";
import MessageBubble from "./MessageBubble";

function ChatWindow({ messages, loading }) {
  const bottomRef = useRef(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({
      behavior: "smooth",
    });
  }, [messages, loading]);

  return (
    <div className="flex-1 overflow-y-auto p-6 bg-gray-50">
      {messages.map((msg, index) => (
        <MessageBubble key={index} message={msg} />
      ))}

      {loading && (
        <MessageBubble
          message={{
            sender: "ai",
            text: "🤖 BP Poddar AI is thinking...",
          }}
        />
      )}

      <div ref={bottomRef}></div>
    </div>
  );
}

export default ChatWindow;