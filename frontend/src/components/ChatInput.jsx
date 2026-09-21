function ChatInput() {

  return (
    <div className="bg-white p-4 border-t">

      <div className="flex gap-3">

        <input
          className="flex-1 border rounded-xl p-3"
          placeholder="Ask about syllabus, faculty, semester..."
        />

        <button className="bg-blue-600 text-white px-5 rounded-xl">
          Send
        </button>

      </div>

    </div>
  );
}

export default ChatInput;