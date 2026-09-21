import { useState } from "react";
import { askAI } from "../services/api";

function ChatInput({ messages, setMessages }) {

    const [question, setQuestion] = useState("");

    async function handleSend() {

        if (!question.trim()) return;

        const userMessage = {
            sender: "user",
            text: question,
        };

        setMessages([...messages, userMessage]);

        const currentQuestion = question;
        setQuestion("");

        const result = await askAI(currentQuestion);

        const aiMessage = {
            sender: "ai",
            text: result.answer,
        };

        setMessages(prev => [...prev, userMessage, aiMessage]);
    }

    return (
        <div className="bg-white p-4 border-t">

            <div className="flex gap-3">

                <input
                    className="flex-1 border rounded-xl p-3"
                    placeholder="Ask anything about BP Poddar..."
                    value={question}
                    onChange={(e) => setQuestion(e.target.value)}
                />

                <button
                    onClick={handleSend}
                    className="bg-blue-600 text-white px-5 rounded-xl"
                >
                    Send
                </button>

            </div>

        </div>
    );
}

export default ChatInput;