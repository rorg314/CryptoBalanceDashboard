import React, { Component } from "react";

import { Tabs, Tab } from "react-bootstrap";
import Wallet from "./wallet.jsx";
import { FetchWallet, FetchAllWallets } from "../coinbase/wallets";

class Dashboard extends React.Component {
  state = {
    wallets: [
      { balance: "1", coin: "1" },
      { balance: "2", coin: "2" },
      { balance: "3", coin: "3" },
    ],
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

export default Dashboard;
