import { useState } from "react";

import Sidebar from "./components/Sidebar";
import Header from "./components/Header";
import ChatWindow from "./components/ChatWindow";
import ChatInput from "./components/ChatInput";

function App() {
    const [messages, setMessages] = useState([
        {
            sender: "ai",
            text: "Hello Sambit! 👋 Ask me anything about BP Poddar."
        }
    ]);

    return (
        <div className="flex h-screen bg-gray-100">
            <Sidebar />

            <div className="flex flex-col flex-1">
                <Header />

                <ChatWindow messages={messages} />

                <ChatInput
                    messages={messages}
                    setMessages={setMessages}
                />
            </div>
        </div>
    );
}

export default App;