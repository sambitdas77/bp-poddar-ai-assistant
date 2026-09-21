
import { useState } from "react";
import { askAI } from "../services/api";

function ChatInput({
  messages,
  setMessages,
  loading,
  setLoading,
}) {
  const [question, setQuestion] = useState("");

  async function handleSend() {
    if (!question.trim() || loading) return;

    const currentQuestion = question;

    const userMessage = {
      sender: "user",
      text: currentQuestion,
    };

    setMessages((prev) => [...prev, userMessage]);

    setQuestion("");

    setLoading(true);

    try {
      const result = await askAI(currentQuestion);

      const aiMessage = {
        sender: "ai",
        text: result.answer,
        sources: result.sources,
      };

      setMessages((prev) => [...prev, aiMessage]);
    } catch (error) {
      const errorMessage = {
        sender: "ai",
        text: "⚠️ Unable to contact the AI server. Please make sure FastAPI is running.",
      };

      setMessages((prev) => [...prev, errorMessage]);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="bg-white border-t p-4">
      <div className="flex gap-3">
        <input
          type="text"
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === "Enter") {
              handleSend();
            }
          }}
          placeholder="Ask anything about BP Poddar..."
          className="flex-1 border border-gray-300 rounded-xl px-4 py-3 outline-none focus:ring-2 focus:ring-blue-500"
        />

        <button
          onClick={handleSend}
          disabled={loading}
          className="bg-blue-600 text-white px-6 rounded-xl hover:bg-blue-700 disabled:bg-gray-400"
        >
          {loading ? "Thinking..." : "Send"}
        </button>
      </div>
    </div>
  );
}

export default ChatInput;