import React, { Component } from "react";
import { Tabs, Tab } from "react-bootstrap";
// Component to hold individual coin statistics

class Wallet extends React.Component {
  render() {
    //console.log("Creating wallet: State: ", this.state, "Props: ", this.props);

    return (
      <div>
        <h2>
          Balance: {this.props.wallet.balance + " " + this.props.wallet.coin}{" "}
        </h2>
        <h2 style={{ color: "green" }}>
          High: $
          {Object.values(this.props.wallet.dateCumlBalUSDSparse).pop()[0]}
        </h2>
        <h2 style={{ color: "red" }}>
          Low: ${Object.values(this.props.wallet.dateCumlBalUSDSparse).pop()[1]}
        </h2>
      </div>
    );
  }
}

export default Wallet;
