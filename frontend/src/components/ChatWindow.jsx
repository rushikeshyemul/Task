import React, { useState } from "react";
import MessageList from "./MessageList";
import UserInput from "./UserInput";
import "./ChatWindow.css";

const ChatWindow = () => {
  const [messages, setMessages] = useState([]);

  const handleSend = async (text) => {
    const userMessage = { sender: "user", text };
    setMessages((prev) => [...prev, userMessage]);

    try {
      const res = await fetch("http://localhost:5000/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: text }),
      });
      const data = await res.json();
      const aiMessage = { sender: "ai", text: data.response };
      setMessages((prev) => [...prev, aiMessage]);
    } catch (error) {
      console.error("Error fetching AI response:", error);
    }
  };

  return (
    <div className="chat-window">
      <h2>E-Commerce AI Assistant</h2>
      <MessageList messages={messages} />
      <UserInput onSend={handleSend} />
    </div>
  );
};

export default ChatWindow;
