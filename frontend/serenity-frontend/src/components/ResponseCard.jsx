// src/components/ResponseCard.jsx

import React from "react";
import "../styles/ResponseCard.css";

const ResponseCard = ({ title, message }) => {
  return (
    <div className="response-card">
      <h3>{title}</h3>
      <p>{message}</p>
    </div>
  );
};

export default ResponseCard;
