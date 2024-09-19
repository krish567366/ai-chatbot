// src/components/Message.js
import React from 'react';

function Message({ text, sender, onFeedback }) {
    return (
        <div className={`message ${sender}`}>
            <p>{text}</p>
            {sender === 'bot' && (
                <div className="feedback">
                    <button onClick={() => onFeedback('positive')}>👍</button>
                    <button onClick={() => onFeedback('negative')}>👎</button>
                </div>
            )}
        </div>
    );
}

export default Message;
