import React, { Component } from "react";

import { Tabs, Tab } from "react-bootstrap";
import Wallet from "./wallet";
import { FetchWallet, FetchAllWallets } from "../coinbase/wallets";

class Dashboard extends React.Component {
  render() {
    return (
      <React.Fragment>
        <div>
          <h1>Dashboard</h1>
        </div>

        <div id="dashCoinTabsDiv">
          <Tabs id="dashCoinTabs">
            {this.props.wallets.map((wallet) => {
              <Wallet wallet={wallet} />;
            })}
          </Tabs>
        </div>
      </React.Fragment>
    );
  }
}

export default Dashboard;
