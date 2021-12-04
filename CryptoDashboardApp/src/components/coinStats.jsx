import React, { Component } from "react";

// Component to hold individual coin statistics
class CoinStats extends React.Component {
  constructor(props) {
    super(props);

    this.coin = props.coin;
    this.state = { balance: 0 };
    //this.processWallet().then((res) => this.setState(res));
    //this.stats = this.processWallet().then((res) => console.log(res));
    //   .then((res) => this.setState(res))
    //   .then(console.log(this.state));
  }

  //   processWallet() {
  //     console.log("Getting " + this.coin + " wallet");

  //     return FetchWallet(this.coin).then((res) =>
  //       ProcessWalletStats(this.coin, res)
  //     );
  //   }

  render() {
    return (
      <div>
        <ul>
          <li>
            <h2>Balance: {this.state.balanceUSD}</h2>
          </li>
        </ul>
      </div>
    );
  }
}

export default CoinStats;
