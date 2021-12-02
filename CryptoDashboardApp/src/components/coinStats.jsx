import React, { Component } from "react";
import GetWalletsPromise from "../coinbase/wallets.js";

// Component to hold individual coin statistics
class CoinStats extends React.Component {
  constructor(props) {
    super(props);

    const wallets = GetWalletsPromise().then((res) => console.log(res));
  }

  render() {
    return (
      <div>
        <ul>
          <li>
            <h2>Balance: {}</h2>
          </li>
        </ul>
      </div>
    );
  }
}

export default CoinStats;
