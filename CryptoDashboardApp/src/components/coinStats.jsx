import React, { Component } from "react";

import FetchWalletData from "../coinbase/wallets.js";

// Component to hold individual coin statistics
class CoinStats extends React.Component {
  constructor(props) {
    super(props);

    //const wallets = GetWalletsPromise().then((res) => console.log(res));

    this.coin = props.coin;

    //console.log(wallet);
  }

  getCoinStats() {
    console.log("Getting coin stats for " + this.coin);
    var wallet = FetchWalletData(this.coin).then((res) => console.log(res));
  }

  render() {
    this.getCoinStats();

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
