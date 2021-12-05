import React, { Component } from "react";
import { Tabs, Tab } from "react-bootstrap";
// Component to hold individual coin statistics

class Wallet extends React.Component {
  state = {
    wallet: { balance: 0 },
  };

  // Map the promise wallet from props into the state
  // constructor(props) {
  //   super(props);

  //   props.wallet.then((res) => {
  //     this.state = { wallet: res };
  //   });
  // }

  componentDidMount() {
    console.log("Wallet mounted", this.props.wallet);
    this.props.wallet.then((res) => {
      this.setState({ wallet: res });
    });
  }

  render() {
    console.log("Creating wallet: State: ", this.state);

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

export default Wallet;
