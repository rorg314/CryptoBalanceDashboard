import React, { Component } from "react";

import { Tabs, Tab } from "react-bootstrap";
import Wallet from "./wallet.jsx";
import { FetchAllWallets, FetchAllWalletsOld } from "../coinbase/wallets";

class Dashboard extends React.Component {
  state = {
    wallets: [],
  };

  componentDidMount() {
    // Load wallets from local JSON (old)
    // FetchAllWalletsOld(this.props.coins).then((res) => {
    //   this.setState({ wallets: res });
    // });

    // Fetch data from the backend API (data values are JSON strings so must parse)
    FetchAllWallets().then((res) => {
      //console.log(res);
      this.setState({ wallets: Object.values(res) });
    });

    //FetchAllWallets(this.props.coins).then((res) => console.log(res));
  }

  render() {
    console.log("Dashboard render: State: ", this.state);

    if (this.state.wallets.length === 0) {
      return <h2>Wallets loading ...</h2>;
    } else {
      return (
        <div
          className="m-4"
          style={{
            width: "90vw",
            margin: "auto",
            padding: "10px",
            position: "relative",
          }}
        >
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
        </div>
      );
    }
  }
}

export default Dashboard;
