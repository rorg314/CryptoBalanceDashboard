import logo from "./logo.svg";

import { Tabs, Tab } from "react-bootstrap";
import React, { Component } from "react";

import Wallet from "./components/wallet";
import Dashboard from "./components/dashboard";
import { FetchWallet, FetchAllWallets } from "./coinbase/wallets";

class App extends React.Component {
  state = {
    coins: ["BTC", "ETH", "DOGE"],
  };

  render() {
    return (
      <div className="text-monospace">
        <nav className="navbar navbar-dark fixed-top bg-dark flex-md-nowrap p-0 shadow">
          <img src={logo} className="App-logo" alt="logo" height="32" />
        </nav>

        <div className="container-fluid mt-5 text-center">
          <div className="row">
            <main role="main" className="col-lg-12 d-flex text-center">
              <div className="content mr-auto ml-auto">
                <div>
                  <h1>Dashboard</h1>
                </div>

                <Dashboard coins={this.state.coins} />
              </div>
            </main>
          </div>
        </div>
      </div>
    );
  }
}

export default App;
