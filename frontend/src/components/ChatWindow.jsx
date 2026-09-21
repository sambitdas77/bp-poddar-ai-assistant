import MessageBubble from "./MessageBubble";

function ChatWindow() {

  const messages = [
    {
      sender: "ai",
      text: "Hello Sambit 👋 Ask me anything about BP Poddar."
    }
  ];

  return (
    <div className="flex-1 overflow-y-auto p-6">

      {messages.map((msg, index) => (
        <MessageBubble key={index} message={msg}/>
      ))}

    </div>
  );
}

export default ChatWindow;