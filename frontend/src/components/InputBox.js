// src/components/InputBox.js
import React, { useState } from 'react';
import axios from '../api';

function InputBox({ addMessage }) {
    const [input, setInput] = useState('');

    const handleSend = async () => {
        if (input.trim() === '') return;

        // Add user message to chat
        addMessage(input, 'user');

        // Call backend API
        try {
            const response = await axios.post('/predict', { text: input });
            const prediction = response.data;

            // Add bot's message with prediction result
            addMessage(`Prediction: ${prediction.label} (Confidence: ${prediction.score})`, 'bot');
        } catch (error) {
            addMessage("Error: Unable to process request.", 'bot');
        }

        // Clear input field
        setInput('');
    };

    return (
        <div className="input-box">
            <input
                type="text"
                value={input}
                onChange={(e) => setInput(e.target.value)}
                placeholder="Type your message..."
            />
            <button onClick={handleSend}>Send</button>
        </div>
    );
}

export default InputBox;
