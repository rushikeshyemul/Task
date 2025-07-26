import React from "react";
import { useChat } from "../context/ChatContext";
import MessageList from "./MessageList";
import UserInput from "./UserInput";
import ConversationHistory from "./ConversationHistory";
import "./ChatWindow.css";

const ChatWindow = () => {
  const { messages } = useChat();

  return (
    <div className="chat-window">
      <ConversationHistory />
      <div className="chat-main">
        <MessageList messages={messages} />
        <UserInput />
      </div>
    </div>
  );
};

export default ChatWindow;
