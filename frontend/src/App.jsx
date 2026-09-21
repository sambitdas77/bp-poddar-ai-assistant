
import { useState } from "react";

import Sidebar from "./components/Sidebar";
import Header from "./components/Header";
import ChatWindow from "./components/ChatWindow";
import ChatInput from "./components/ChatInput";

function App() {
  const [messages, setMessages] = useState([
    {
      sender: "ai",
      text: "Hello Sambit! 👋 I am BP Poddar AI Assistant. Ask me anything about your college, syllabus, or semester.",
      sources: [],
    },
  ]);

  const [loading, setLoading] = useState(false);

  return (
    <div className="flex h-screen bg-gray-100">
      <Sidebar />

      <div className="flex flex-col flex-1">
        <Header />

        <ChatWindow messages={messages} loading={loading} />

        <ChatInput
          messages={messages}
          setMessages={setMessages}
          loading={loading}
          setLoading={setLoading}
        />
      </div>
    </div>
  );
}

export default App;