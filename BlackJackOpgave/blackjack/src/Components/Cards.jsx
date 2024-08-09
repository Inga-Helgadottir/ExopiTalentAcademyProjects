import React from "react";
import Card from "./Card";
import back from "../Images/backOfCards.jpg";

const Cards = (props) => {
  return (
    <div id={props.whichCards ? "winLooseBoxCardStyles" : ""}>
      {props.isBetPlaced && (
        <div>
          <h2 className="dealerHeadline">The dealer</h2>
          <div className="theDealer">
            {!props.whichCards && (
              <img
                src={back}
                alt="card faced down"
                className="card"
                style={{
                  display: props.isDealersCardFaceUp ? "none" : "block",
                }}
              />
            )}
            {props.dealerCards.map(function (dCard, index) {
              return <Card key={index} props={dCard} />;
            })}
          </div>
        </div>
      )}
      <div className="player">
        <h2 className="playerHeadline">{props.currentPlayer.name}</h2>
        {props.isBetPlaced && (
          <div className="playerCards">
            {props.playerCards.map(function (pCard, index) {
              return <Card key={index} props={pCard} />;
            })}
          </div>
        )}
      </div>
    </div>
  );
};

export default Cards;
