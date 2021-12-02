import React, { Component } from "react";
import GetPrice from "../coinbase/prices.js";

import FetchWallet from "../coinbase/wallets.js";

// Process the wallet into the stats object
async function ProcessWalletStats(coin, wallet) {
  var balance = wallet["balance"];

  var stats = {
    balance: balance,
    balanceUSD: GetPrice(coin, "2021-12-01").then((response) =>
      response.map((el) => el * stats.balance)
    ),
  };
  return stats;
}

// Component to hold individual coin statistics
class CoinStats extends React.Component {
  constructor(props) {
    super(props);

    this.coin = props.coin;
  }

  processWallet() {
    console.log("Getting " + this.coin + " wallet");
    var wallet = FetchWallet(this.coin).then((res) =>
      ProcessWalletStats(this.coin, res)
    );
  }

  render() {
    this.processWallet();

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
