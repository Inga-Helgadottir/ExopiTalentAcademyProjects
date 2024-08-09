import heart from "./Images/Heart.png";
import spade from "./Images/Spade.png";
import diamond from "./Images/Diamond.png";
import club from "./Images/Club.png";
import "./App.css";
import { useState } from "react";
import TheGame from "./Components/TheGame";

function App() {
  const [isStartButtonDisplayed, setIsStartButtonDisplayed] = useState(true);

  return (
    <div className="App">
      <header id="headerStyles" className="redThemeColor">
        <img src={heart} alt="heart" className="hsdc" />
        <img src={spade} alt="spade" className="hsdc" />
        Blackjack
        <img src={diamond} alt="diamond" className="hsdc" />
        <img src={club} alt="club" className="hsdc" />
      </header>

      {isStartButtonDisplayed && (
        <button
          className="startBtn btn"
          onClick={(e) => {
            setIsStartButtonDisplayed(!isStartButtonDisplayed);
          }}
        >
          Start a game
        </button>
      )}

      {!isStartButtonDisplayed && (
        <div className="container">
          <TheGame />
        </div>
      )}
    </div>
  );
}

export default App;
