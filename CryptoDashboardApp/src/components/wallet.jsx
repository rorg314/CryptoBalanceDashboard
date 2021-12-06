import React, { Component } from "react";
import { Tabs, Tab } from "react-bootstrap";
// Component to hold individual coin statistics

class Wallet extends React.Component {
  render() {
    //console.log("Creating wallet: State: ", this.state, "Props: ", this.props);
    console.log(typeof this.props.wallet.cumlBalancesUSDSparse);
    return (
      <div>
        <h2>
          Balance: {this.props.wallet.balance + " " + this.props.wallet.coin}{" "}
        </h2>
        <h2 style={{ color: "green" }}>
          High: $
          {Object.values(this.props.wallet.cumlBalancesUSDSparse).pop()[0]}
        </h2>
        <h2 style={{ color: "red" }}>
          Low: $
          {Object.values(this.props.wallet.cumlBalancesUSDSparse).pop()[1]}
        </h2>
      </div>
    );
  }
}

export default Wallet;
