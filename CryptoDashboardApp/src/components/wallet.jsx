import React, { Component } from "react";
import { Tabs, Tab } from "react-bootstrap";
// Component to hold individual coin statistics

class Wallet extends React.Component {
  render() {
    console.log("Creating wallet", this.props.wallet);

    return (
      <div>
        <ul>
          <li>
            <h2>Balance: {this.props.wallet.balance}</h2>
          </li>
        </ul>
      </div>
    );
  }
}

export default Wallet;
