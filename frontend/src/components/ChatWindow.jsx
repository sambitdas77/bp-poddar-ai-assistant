import MessageBubble from "./MessageBubble";

function ChatWindow({ messages }) {

    return (
        <div className="flex-1 overflow-y-auto p-6">

            {messages.map((msg, index) => (
                <MessageBubble
                    key={index}
                    message={msg}
                />
            ))}

        </div>
    );
}

export default ChatWindow;