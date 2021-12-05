import React, { Component } from "react";

import { Tabs, Tab } from "react-bootstrap";
import Wallet from "./wallet";
import { FetchWallet, FetchAllWallets } from "../coinbase/wallets";

class Dashboard extends React.Component {
  state = {
    wallets: [{ balance: "hi" }],
  };

  componentDidMount() {
    // Load wallets
    FetchAllWallets(this.props.coins).then((res) => {
      this.setState({ wallets: res });
    });

    //.then((res) => console.log("Set state", res));
  }

  render() {
    console.log("Dashboard render: State: ", this.state);

    return (
      <Tabs id="dashCoinTabs">
        {this.state.wallets.map((w) => {
          <Wallet key={w.coin} wallet={w} />;
        })}
      </Tabs>
    );
  }
}

export default Dashboard;
