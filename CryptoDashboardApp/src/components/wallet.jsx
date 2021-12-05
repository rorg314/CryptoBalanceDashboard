import React, { Component } from "react";
import { Tabs, Tab } from "react-bootstrap";
// Component to hold individual coin statistics
class Wallet extends React.Component {
  render() {
    console.log("Creating wallet", this.props.wallet);

    return (
      <Tab
        eventKey={"wallet" + this.props.wallet.coin}
        title={this.props.wallet.coin}
      >
        <div>
          <ul>
            <li>
              <h2>Balance: {this.props.wallet.balance}</h2>
            </li>
          </ul>
        </div>
      </Tab>
    );
  }
}

export default Wallet;
