import React from 'react';
import Chatbot from './Chatbot';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src="gdglemanslogo.webp"/> 
        <h1>AI Chatbot</h1>
      </header>
      <main>
        <Chatbot/>
      </main>
    </div>
  );
}

export default App;
