import React from "react";
import { useState, useEffect } from "react";

import back from "../Images/backOfCards.jpg";
import chip from "../Images/chip.svg";
import Cards from "./Cards";
import Player from "./Player";

const TheGame = () => {
  // the deck of cards
  const [deckOfCards, setDeckOfCards] = useState([]);

  // the current player and their cards
  const [currentPlayer, setCurrentPlayer] = useState(new Player("Hannah", 500));
  const [playerCards, setPlayerCards] = useState([]);

  // the dealers cards
  const [dealerCards, setDealerCards] = useState([]);
  const [allDealerCards, setAllDealerCards] = useState([]);
  const [dealerHiddenCard, setDealerHiddenCard] = useState({});
  // is the dealers card upside down
  const [isDealersCardFaceUp, setIsDealersCardFaceUp] = useState(false);

  // starter values
  const [placedBets, setPlacedBets] = useState(0);
  const [isBetPlaced, setIsBetPlaced] = useState(false);
  const [blackjackOrTwentyOne, setBlackjackOrTwentyOne] = useState("blackjack");

  const [isGameOver, setIsGameOver] = useState(false);
  const [winOrLooseText, setWinOrLooseText] = useState("");
  const [areThereNoMoreChips, setAreThereNoMoreChips] = useState(true);

  // the minimum and maximum amount you can bet and the amount of decks in the game (these variables are used for every reference)
  const minBet = 50;
  const maxBet = 500;
  const amountOfDecksInGame = 4;

  // button functions
  const [hit, setHit] = useState(false);
  const [stand, setStand] = useState(false);

  // constantly checking for a bust and a blackjack
  useEffect(() => {
    checkForBustAndBL();
    if (currentPlayer.chipCount <= 0 && isGameOver === true) {
      setAreThereNoMoreChips(false);
      getWinOrLooseBox("Game over, You are out of chips");
    }
  });

  // combining the dealers cards
  const getAllDealersCards = () => {
    if (allDealerCards.length === 0) {
      for (let i = 0; i < dealerCards.length; i++) {
        allDealerCards.push(dealerCards[i]);
      }

      allDealerCards.push(dealerHiddenCard);
      setDealerCards(allDealerCards);
    }
    return allDealerCards;
  };

  // stand button was clicked, the player does not want more cards so it's the dealers turn
  const standFunc = () => {
    if (placedBets !== 0 && isGameOver === false) {
      setStand(!stand);
      dealersTurn();
    }
  };

  // hit button was clicked, the player wants another card
  const hitFunc = () => {
    if (placedBets !== 0 && isGameOver === false) {
      setHit(!hit);
      setBlackjackOrTwentyOne("21");
      getRandomCard("player");
    }
  };

  const checkForBustAndBL = () => {
    if (playerCards.length !== 0) {
      let player = getCardValues(playerCards);

      if (player === 21) {
        dealersTurn();
      } else if (player > 21) {
        // hides the face down card
        setIsDealersCardFaceUp(true);

        // replacing the card i hid
        allDealerCards.push(getRandomCard("dealer"));

        getWinOrLooseBox("Sorry you busted");
      }
    }
  };

  const findWinner = () => {
    let messageArray = [
      "Congratulations, you won!!",
      "Sorry, it's a tie",
      "Sorry, you lost",
      "Congratulations, you got " + blackjackOrTwentyOne + "!!",
    ];
    let messageArrayIndex;

    let player = getCardValues(playerCards);
    let dealer = getCardValues(getAllDealersCards());

    if (player === 21 && dealer !== 21) {
      messageArrayIndex = 3;

      if (blackjackOrTwentyOne === "21") {
        addToPlayersChipCount(2);
      } else {
        addToPlayersChipCount(3);
      }
    } else if (player === 21 && dealer === 21) {
      messageArrayIndex = 1;
    } else if (
      (player !== 21 && dealer === 21) ||
      (player > 21 && dealer > 21)
    ) {
      messageArrayIndex = 2;
    } else if (player < 21 && dealer > 21) {
      messageArrayIndex = 0;
      addToPlayersChipCount(2);
    } else {
      if (player === dealer) {
        messageArrayIndex = 1;
      } else if (player < dealer) {
        messageArrayIndex = 2;
      } else if (player > dealer) {
        messageArrayIndex = 0;
        addToPlayersChipCount(2);
      } else {
        messageArrayIndex = 1;
      }
    }

    getWinOrLooseBox(messageArray[messageArrayIndex]);
  };

  const addToPlayersChipCount = (amount) => {
    currentPlayer.chipCount += placedBets * amount;
  };

  const getWinOrLooseBox = (text) => {
    window.scrollTo(0, 0);
    setIsGameOver(true);
    setWinOrLooseText(text);
  };

  const checkForAces = (cards) => {
    let acesPresent = 0;

    // loop through the cards to check
    for (let i = 0; i < cards.length; i++) {
      // checking if it's an Ace
      if (cards[i].name === "A") {
        acesPresent += 1;
      }
    }
    return acesPresent;
  };

  const whatValueShouldTheAcesBe = (cards) => {
    let value = 0;
    // acesPresent returns the amount of Aces in the cards
    let acesPresent = checkForAces(cards);

    let cardsWithoutAces = [];

    if (cards.length !== undefined) {
      // loop through the cards
      cards.forEach((card) => {
        if (card.name !== "A") {
          // push all aces to the cardsWithoutAces array
          cardsWithoutAces.push(card);
        }
      });

      // getting the values of the cards that arent aces
      let valuesWithoutAces = getCardValues(cardsWithoutAces);

      // if there are 2 or more aces and the other values are 9 or smaller
      if (acesPresent >= 2 && valuesWithoutAces <= 9) {
        // then add 11
        value += 11;

        // loop through the rest and give each the value 1
        for (let i = 1; i <= acesPresent; i++) {
          value += 1;
        }

        // if there is 1 ace and the other values are more than 10
      } else if (valuesWithoutAces > 10 && acesPresent === 1) {
        // then the ace should be 1
        value = 1;
      } else {
        // if none of those conditions are met give the ace 11
        value = 11;
      }
    } else {
      value = 11;
    }
    return value;
  };

  const dealersTurn = () => {
    // hides the face down card
    setIsDealersCardFaceUp(true);

    // gets the value of all of the dealers cards
    let dealer = getCardValues(getAllDealersCards());

    while (dealer < 18) {
      // the dealer gets a new card if the total value of their cards are under 17
      allDealerCards.push(getRandomCard("dealer"));

      // getting the new values so the while loop goes on if the value is still under 17
      dealer = getCardValues(allDealerCards);
    }

    findWinner();
  };

  const singleCardFunc = (nameVar, suitVar) => {
    let singleCard = {
      name: nameVar,
      suit: suitVar,
    };

    deckOfCards.push(singleCard);
  };

  const MakeDeckOfCards = () => {
    if (deckOfCards.length === 0) {
      // 1st loop is to make multible decs in the game controlled by a variable
      for (let ii = 0; ii < amountOfDecksInGame; ii++) {
        // 2nd loop is to get every card in every suit
        for (let i = 0; i < 4; i++) {
          const suits = ["Heart", "Spade", "Diamond", "Club"];

          // 3rd loop is to get the cards between 2 and 10
          for (let x = 2; x < 11; x++) {
            singleCardFunc(x, suits[i]);
          }
          // making the face cards
          singleCardFunc("J", suits[i]);
          singleCardFunc("Q", suits[i]);
          singleCardFunc("K", suits[i]);
          singleCardFunc("A", suits[i]);
        }
      }
    }
  };

  const getCardValues = (cards) => {
    // a variable to add the values to
    let values = 0;

    // loop through the cards to check
    for (let i = 0; i < cards.length; i++) {
      // isNaN returns true if its not a number
      if (isNaN(cards[i].name)) {
        // checking if it's an Ace
        if (cards[i].name === "A") {
          values += whatValueShouldTheAcesBe(cards);

          // checks for the other face cards
        } else {
          values += 10;
        }

        // gets the rest of the cards
      } else {
        values += cards[i].name;
      }
    }
    return values;
  };

  const getRandomCard = (playerOrDealer) => {
    const min = 0;
    const max = deckOfCards.length - 1;

    const randomNbr = Math.floor(min + Math.random() * (max - min));
    let randomCard = deckOfCards[randomNbr];
    deckOfCards.splice(deckOfCards.indexOf(randomCard) - 1, 1);

    if (playerOrDealer === "player") {
      playerCards.push(randomCard);
    } else if (playerOrDealer === "dealer") {
      dealerCards.push(randomCard);
    } else {
      setDealerHiddenCard(randomCard);
    }
    return randomCard;
  };

  const getStarterCards = () => {
    getRandomCard("player");
    getRandomCard("player");
    getRandomCard("dealer");
    getRandomCard("dealers hidden card (getRandomCard else)");
  };

  const placeABet = (e) => {
    let inputValue = parseInt(e.target.previousSibling.value);
    let chipCountMinusInputValue = currentPlayer.chipCount - inputValue;

    let nanCheck = inputValue !== NaN;
    let emptyCheck = inputValue !== "";
    let MinMaxCheck = inputValue >= minBet && inputValue <= maxBet;

    if (nanCheck && emptyCheck && !MinMaxCheck) {
      alert("You have to place a bet between " + minBet + " and " + maxBet);
    } else if (chipCountMinusInputValue >= 0) {
      setPlacedBets(inputValue);
      setIsBetPlaced(true);

      currentPlayer.chipCount = chipCountMinusInputValue;

      MakeDeckOfCards();
      getStarterCards();
    } else {
      alert("You don't have enough money to place that bet");
    }
  };

  const startOver = () => {
    setDeckOfCards([]);

    setPlayerCards([]);

    setDealerCards([]);
    setDealerHiddenCard({});
    setIsDealersCardFaceUp(false);
    setAllDealerCards([]);

    setIsBetPlaced(false);
    setPlacedBets(0);
    setIsGameOver(false);
    setAreThereNoMoreChips(true);

    setStand(false);
    setHit(false);

    setBlackjackOrTwentyOne("blackjack");
    setWinOrLooseText("");

    MakeDeckOfCards();
  };

  const getMoreChips = () => {
    currentPlayer.chipCount += maxBet;
    startOver();
  };

  const getCards = (whichCardsID) => {
    let whichCards = whichCardsID === 1;
    return (
      <Cards
        whichCards={whichCards}
        playerCards={playerCards}
        currentPlayer={currentPlayer}
        dealerCards={dealerCards}
        isDealersCardFaceUp={isDealersCardFaceUp}
        isBetPlaced={isBetPlaced}
      />
    );
  };

  return (
    <div className="table">
      {isGameOver && (
        <div className="winOrLooseInfoBox">
          <h1>{winOrLooseText}</h1>
          {getCards(1)}
          {areThereNoMoreChips ? (
            <button className="startBtn btn" onClick={startOver}>
              Play again
            </button>
          ) : (
            <button className="startBtn btn" onClick={getMoreChips}>
              Get more chips and play again
            </button>
          )}
        </div>
      )}
      <div className="secondTable">
        <div className="showCardContainer">
          <div className="betsAndDeck">
            <div className="bets">
              <h2>
                Bets
                <br />
                <span style={{ fontSize: "15px", textDecoration: "none" }}>
                  Min: {minBet} - Max: {maxBet}
                </span>
              </h2>
              <img src={chip} alt="chip" className="chip" />
              <p>{placedBets}</p>
            </div>
            <img
              src={back}
              alt="deck of cards faced down"
              className="facedDownDeck card"
              style={{ display: isBetPlaced ? "block" : "none" }}
            />
          </div>
          {!isBetPlaced && (
            <div className="theBetSize">
              <h2>How much would you like to bet?</h2>
              <input
                type="number"
                name="betToPlace"
                min={minBet}
                max={maxBet}
              />
              <button className="btn hitBtn" onClick={placeABet}>
                Place bet
              </button>
            </div>
          )}

          <div>
            <div>
              {getCards(0)}
              <div className="bettingChips">
                {currentPlayer.chipCount}{" "}
                <img src={chip} alt="chip" className="chip" />
              </div>
            </div>
          </div>
          {isBetPlaced && (
            <div className="playerButtons">
              <button onClick={hitFunc} className="btn hitBtn">
                Hit
              </button>
              <button onClick={standFunc} className="btn standBtn">
                Stand
              </button>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};
export default TheGame;
