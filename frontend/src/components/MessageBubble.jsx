
function MessageBubble({ message }) {
  const isAI = message.sender === "ai";

  return (
    <div className={`flex mb-5 ${isAI ? "justify-start" : "justify-end"}`}>
      <div
        className={`
          max-w-[75%] px-5 py-3 rounded-2xl shadow-md
          ${
            isAI
              ? "bg-white text-gray-800 rounded-bl-md"
              : "bg-blue-600 text-white rounded-br-md"
          }
        `}
      >
        <p className="whitespace-pre-wrap">{message.text}</p>

        {message.sources && message.sources.length > 0 && (
          <div className="mt-3 pt-2 border-t border-gray-200 text-xs text-blue-600">
            📄 Sources: {message.sources.join(", ")}
          </div>
        )}
      </div>
    </div>
  );
}

export default MessageBubble;