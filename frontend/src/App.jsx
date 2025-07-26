// App.jsx
import React from "react";
import { ChatProvider } from "./context/ChatContext";
import ChatWindow from "./components/ChatWindow";
import UserInput from "./components/UserInput";
import "./App.css";

const App = () => {
  return (
    <ChatProvider>
      <div className="app">
        <h2>Conversational AI</h2>
        <ChatWindow />
        <UserInput />
      </div>
    </ChatProvider>
  );
};

export default App;
