// components/Sidebar.jsx
import React from "react";
import { useChat } from "../context/ChatContext";
import "./Sidebar.css";

const Sidebar = () => {
  const { history, loadConversation, currentSessionId } = useChat();

  return (
    <div className="sidebar">
      <h3>Conversations</h3>
      {history.length === 0 && <p>No past chats</p>}
      <ul>
        {history.map((session) => (
          <li
            key={session.id}
            className={session.id === currentSessionId ? "active" : ""}
            onClick={() => loadConversation(session.id)}
          >
            Session {new Date(session.id).toLocaleString()}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Sidebar;
