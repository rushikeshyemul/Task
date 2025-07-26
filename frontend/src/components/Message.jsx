import React from "react";
import "./Message.css";

const Message = ({ sender, text }) => {
  const className = sender === "user" ? "message user" : "message ai";
  return <div className={className}>{text}</div>;
};

export default Message;
