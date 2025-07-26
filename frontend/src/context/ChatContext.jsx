import React, { createContext, useContext, useState } from "react";

const ChatContext = createContext();

export const ChatProvider = ({ children }) => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  return (
    <ChatContext.Provider
      value={{
        messages,
        setMessages,
        input,
        setInput,
        loading,
        setLoading,
      }}
    >
      {children}
    </ChatContext.Provider>
  );
};

// Custom hook
export const useChat = () => {
  const context = useContext(ChatContext);
  if (!context) throw new Error("useChat must be used within ChatProvider");
  return context;
};
export { ChatContext };
