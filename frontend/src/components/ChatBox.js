// src/components/ChatBox.js
import React from 'react';
import Message from './Message';

function ChatBox({ messages }) {
    return (
        <div className="chat-box">
            {messages.map((message, index) => (
                <Message key={index} text={message.text} sender={message.sender} />
            ))}
        </div>
    );
}

export default ChatBox;
