import React from "react";
import { useChat } from "../context/ChatContext";
import "./UserInput.css";

const UserInput = () => {
  const { input, setInput, loading, setLoading, messages, setMessages } =
    useChat();

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!input.trim()) return;

    const userMessage = { sender: "user", text: input };
    setMessages((prev) => [...prev, userMessage]);
    setLoading(true);

    try {
      const res = await fetch("http://localhost:5000/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: input }),
      });

      const data = await res.json();
      const aiMessage = { sender: "ai", text: data.reply };
      setMessages((prev) => [...prev, aiMessage]);
    } catch (error) {
      console.error(error);
      setMessages((prev) => [
        ...prev,
        { sender: "ai", text: "Something went wrong. Try again!" },
      ]);
    }

    setLoading(false);
    setInput("");
  };

  return (
    <form className="user-input" onSubmit={handleSubmit}>
      <input
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Type your message..."
      />
      <button type="submit" disabled={loading}>
        {loading ? "Sending..." : "Send"}
      </button>
    </form>
  );
};

export default UserInput;
