// components/ChatWindow.jsx
import React from "react";
import { useChat } from "../context/ChatContext";
import "./ChatWindow.css";

const ChatWindow = () => {
  const { messages, loading } = useChat();

  return (
    <div className="chat-window">
      {messages.map((msg, index) => (
        <div key={index} className={`message ${msg.sender}`}>
          <strong>{msg.sender === "user" ? "You" : "AI"}:</strong> {msg.text}
        </div>
      ))}
      {loading && <div className="message ai">AI is typing...</div>}
    </div>
  );
};

export default ChatWindow;
