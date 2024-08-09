import React, { useEffect } from "react";
import Heart from "../Images/Heart.png";
import Spade from "../Images/Spade.png";
import Diamond from "../Images/Diamond.png";
import Club from "../Images/Club.png";
import { useState } from "react";

const Card = (props) => {
  const [propsAreCorrect, setPropsAreCorrect] = useState(false);

  useEffect(() => {
    if (props !== undefined) {
      if (props.props !== undefined) {
        if (props.props.name !== undefined && props.props.name !== "") {
          setPropsAreCorrect(true);
        }
      }
    } else {
      setPropsAreCorrect(false);
    }
  }, []);

  const getSuitImg = (suit) => {
    switch (suit) {
      case "Heart":
        return <img src={Heart} alt={suit} className="singleCardHsdc" />;
      case "Spade":
        return <img src={Spade} alt={suit} className="singleCardHsdc" />;
      case "Diamond":
        return <img src={Diamond} alt={suit} className="singleCardHsdc" />;
      case "Club":
        return <img src={Club} alt={suit} className="singleCardHsdc" />;
    }
  };

  return (
    <div>
      {propsAreCorrect && (
        <div className="card">
          <h2>{props.props.name}</h2>
          {getSuitImg(props.props.suit)}
        </div>
      )}
    </div>
  );
};

export default Card;
