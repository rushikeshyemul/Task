// src/context/ChatProvider.jsx
import { useState } from "react";
import { ChatContext } from "./ChatContext";

const ChatProvider = ({ children }) => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  const sendMessage = (newMessage) => {
    setMessages((prev) => [...prev, newMessage]);
  };

  return (
    <ChatContext.Provider
      value={{ messages, input, setInput, loading, setLoading, sendMessage }}
    >
      {children}
    </ChatContext.Provider>
  );
};

export default ChatProvider;
