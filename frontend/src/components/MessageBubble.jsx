function MessageBubble({ message }) {

  const isAI = message.sender === "ai";

  return (
    <div className={`flex ${isAI ? "justify-start" : "justify-end"} mb-4`}>

      <div
        className={`
          max-w-lg p-4 rounded-2xl shadow
          ${isAI
            ? "bg-white text-black"
            : "bg-blue-600 text-white"}
        `}
      >
        {message.text}
      </div>

    </div>
  );
}

export default MessageBubble;