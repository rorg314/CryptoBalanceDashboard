import React, { Component } from "react";
import GetWallets from "../coinbase/wallets.js";

// Component to hold individual coin statistics
class CoinStats extends React.Component {
  constructor(props) {
    super(props);
    //console.log(this.props);
    var wallets = GetWallets();

    debugger;
    var wallet;
    if (props["coin"] === "BTC") {
      wallet = wallets[0];
    } else if (props["coin"] === "ETH") {
      wallet = wallets[1];
    } else if (props["coin"] === "DOGE") {
      wallet = wallets[2];
    }
    this.state = { coin: props.coin, wallet: wallet };
  }

  render() {
    return (
      <div>
        <ul>
          <li>
            <h2>Balance: {this.state.wallet.balance}</h2>
          </li>
        </ul>
      </div>
    );
  }
}

export default CoinStats;
