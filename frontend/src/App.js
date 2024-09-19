// src/App.js
import React, { useState } from 'react';
import ChatBox from './components/ChatBox';
import InputBox from './components/InputBox';
import './styles.css';

function App() {
    const [messages, setMessages] = useState([]);

    const addMessage = (message, sender) => {
        setMessages([...messages, { text: message, sender }]);
    };

    return (
        <div className="app-container">
            <h1>AI Chatbot Interface</h1>
            <ChatBox messages={messages} />
            <InputBox addMessage={addMessage} />
        </div>
    );
}

export default App;
