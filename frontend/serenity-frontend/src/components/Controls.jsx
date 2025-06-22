// src/components/Controls.jsx

import React, { useState } from "react";
import "../styles/Controls.css";
import ResponseCard from "./ResponseCard";

const Controls = () => {
  const [response, setResponse] = useState("");
  const [title, setTitle] = useState("");

  const fetchData = async (type) => {
    const endpoints = {
      affirm: "/affirmation",
      motivate: "/motivate",
      tip: "/tip",
    };

    const titles = {
      affirm: "💖 Affirmation",
      motivate: "🔥 Motivation",
      tip: "🌿 Wellness Tip",
    };

    try {
      const res = await fetch(`http://localhost:8000${endpoints[type]}`);
      const data = await res.json();
      setResponse(data.message || data.tip);
      setTitle(titles[type]);
    } catch (err) {
      setResponse("Something went wrong. Please try again.");
      setTitle("Error");
      console.error(err);
    }
  };

  return (
    <div className="controls">
      <h2>Need a quick boost?</h2>
      <div className="button-group">
        <button onClick={() => fetchData("affirm")}>Affirm Me 💖</button>
        <button onClick={() => fetchData("motivate")}>Motivate Me 🔥</button>
        <button onClick={() => fetchData("tip")}>Wellness Tip 🌿</button>
      </div>

      {response && <ResponseCard title={title} message={response} />}
    </div>
  );
};

export default Controls;
