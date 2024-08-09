import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import { BrowserRouter, Routes, Route } from "react-router-dom";

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <BrowserRouter>
  <Routes>
    <Route path="/" element={<App />}></Route>
    <Route
      // default for when the link is wrong
      // like http://localhost:3000/hjklhjklh
      path="*"
      element={
        <main style={{ padding: "1rem" }}>
          <h1 style={{color:"#000", fontSize:"50px"}}>There's nothing here!</h1>
          <p>
            <a href="/" style={{color:"#000", fontSize:"50px"}}>Click here, to go back to Blackjack!</a>
          </p>
        </main>
      }
    />
  </Routes>
</BrowserRouter>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
