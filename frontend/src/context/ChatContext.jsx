import React, { createContext, useContext, useState } from "react";

const ChatContext = createContext();

export const ChatProvider = ({ children }) => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const [sessions, setSessions] = useState([]);
  const [activeSession, setActiveSession] = useState(null);

  const startNewSession = () => {
    const sessionId = Date.now();
    const newSession = { id: sessionId, messages: [] };
    setSessions((prev) => [newSession, ...prev]);
    setMessages([]);
    setActiveSession(sessionId);
  };

  const loadSession = (sessionId) => {
    const session = sessions.find((s) => s.id === sessionId);
    if (session) {
      setMessages(session.messages);
      setActiveSession(sessionId);
    }
  };

  const sendMessage = (message) => {
    setMessages((prev) => {
      const updated = [...prev, message];

      // Save to current session
      setSessions((prevSessions) =>
        prevSessions.map((s) =>
          s.id === activeSession ? { ...s, messages: updated } : s
        )
      );

      return updated;
    });
  };

  return (
    <ChatContext.Provider
      value={{
        messages,
        setMessages,
        input,
        setInput,
        loading,
        setLoading,
        sendMessage,
        sessions,
        startNewSession,
        loadSession,
        activeSession,
      }}
    >
      {children}
    </ChatContext.Provider>
  );
};

export const useChat = () => useContext(ChatContext);
export default ChatContext;
