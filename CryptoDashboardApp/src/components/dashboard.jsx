import React, { Component } from "react";

import { Tabs, Tab } from "react-bootstrap";
import Wallet from "./wallet.jsx";
import { FetchWallet, FetchAllWallets } from "../coinbase/wallets";

class Dashboard extends React.Component {
  state = {
    wallets: [
      // { balance: "hi1", coin: "1" },
      // { balance: "hi2", coin: "2" },
      // { balance: "hi3", coin: "3" },
    ],
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
      <Tabs id="dashboardWalletTabs">
        {this.state.wallets.map((w) => {
          return (
            <Tab
              eventKey={"wallet" + w.coin}
              key={"wallet" + w.coin}
              title={"Wallet " + w.coin}
            >
              <Wallet wallet={w} />
            </Tab>
          );
        })}
      </Tabs>
    );
  }
}

export default Dashboard;
