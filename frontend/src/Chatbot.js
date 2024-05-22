import React, { useState } from 'react';
import './Chatbot.css';

function Chatbot() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');

  const sendMessage = async () => {
    if (input.trim() === '') return;

    const userMessage = { sender: 'user', text: input };
    setMessages([...messages, userMessage]);
    setInput('');

    // Create a new EventSource instance to receive server-sent events
    const eventSource = new EventSource(`http://localhost:3000/stream_log?question=${encodeURIComponent(input)}`);

    // Listen for messages from the server
    eventSource.onmessage = (event) => {
      const botMessage = { sender: 'bot', text: event.data };
      setMessages((prevMessages) => [...prevMessages, botMessage]);
    };

    // Handle any errors that occur
    eventSource.onerror = (error) => {
      console.error('Error receiving message:', error);
      eventSource.close();
    };

    // Close the connection when the user navigates away
    return () => {
      eventSource.close();
    };
  };

  return (
    <div className="chatbot-container">
      <div className="messages-container">
        {messages.map((msg, index) => (
          <div key={index} className={`message ${msg.sender}`}>
            {msg.text}
          </div>
        ))}
      </div>
      <div className="input-container">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={(e) => { if (e.key === 'Enter') sendMessage(); }}
          placeholder="Type your message..."
        />
        <button onClick={sendMessage} className="mat-icon-button"><mat-icon>arrow_upward</mat-icon></button>
      </div>
    </div>
  );
}

export default Chatbot;
