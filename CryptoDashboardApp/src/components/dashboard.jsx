import React, { Component } from "react";

import { Tabs, Tab } from "react-bootstrap";
import Wallet from "./wallet.jsx";
import { FetchWallet, FetchAllWallets } from "../coinbase/wallets";

class Dashboard extends React.Component {
  state = {
    wallets: [],
  };

  componentDidMount() {
    // Load wallets
    FetchAllWallets(this.props.coins).then((res) => {
      this.setState({ wallets: res });
    });

    //FetchAllWallets(this.props.coins).then((res) => console.log(res));
  }

  render() {
    console.log("Dashboard render: State: ", this.state);

    if (this.state.wallets.length === 0) {
      return <h2>Wallets loading ...</h2>;
    } else {
      return (
        <Tabs id="dashboardWalletTabs">
          {this.state.wallets.map((wallet) => {
            return (
              <Tab
                eventKey={"wallet" + wallet.coin}
                key={"wallet" + wallet.coin}
                title={wallet.coin}
              >
                <Wallet wallet={wallet} />
              </Tab>
            );
          })}
        </Tabs>
      );
    }
  }
}

export default Dashboard;
