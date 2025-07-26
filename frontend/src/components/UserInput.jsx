import React, { useState } from "react";
import "./UserInput.css";

const UserInput = ({ onSend }) => {
  const [input, setInput] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (input.trim() !== "") {
      onSend(input);
      setInput("");
    }
  };

  return (
    <form className="user-input" onSubmit={handleSubmit}>
      <input
        type="text"
        value={input}
        placeholder="Ask a question..."
        onChange={(e) => setInput(e.target.value)}
      />
      <button type="submit">Send</button>
    </form>
  );
};

export default UserInput;
