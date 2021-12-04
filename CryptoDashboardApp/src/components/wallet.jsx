import React, { Component } from "react";

// Component to hold individual coin statistics
class Wallet extends React.Component {
  
  state={wallet = this.props.wallet}
  
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

export default Wallet;
