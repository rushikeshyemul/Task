import React from "react";
import { useChat } from "../context/ChatContext";
import "./ConversationHistory.css";

const ConversationHistory = () => {
  const { sessions, loadSession, startNewSession, activeSession } = useChat();

  return (
    <div className="history-panel">
      <h3>Conversations</h3>
      <button onClick={startNewSession}>+ New Chat</button>
      <ul>
        {sessions.map((s) => (
          <li
            key={s.id}
            className={s.id === activeSession ? "active" : ""}
            onClick={() => loadSession(s.id)}
          >
            Session {new Date(s.id).toLocaleString()}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ConversationHistory;
