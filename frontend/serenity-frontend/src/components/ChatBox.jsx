// src/components/ChatBox.jsx

import React, { useState } from "react";
import "../styles/ChatBox.css";

const ChatBox = () => {
  const [message, setMessage] = useState("");
  const [reply, setReply] = useState(null);
  const [mood, setMood] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSend = async () => {
    if (!message.trim()) return;
    setLoading(true);

    try {
      const res = await fetch("http://localhost:8000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message }),
      });

      const data = await res.json();
      setReply(data.reply);
      setMood(data.mood);
      setMessage("");
    } catch (err) {
      console.error("Error:", err);
      setReply("Something went wrong. Please try again.");
      setMood("😕");
    }

    setLoading(false);
  };

  return (
    <div className="chatbox">
      <h2>Talk to SerenityAI</h2>

      <div className="chat-input-group">
        <input
          type="text"
          placeholder="How are you feeling?"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
        />
        <button onClick={handleSend} disabled={loading}>
          {loading ? "Thinking..." : "Send"}
        </button>
      </div>

      {reply && (
        <div className="chat-response">
          <p>{reply}</p>
          <span className="mood">{mood}</span>
        </div>
      )}
    </div>
  );
};

export default ChatBox;
