import logo from "./logo.svg";

import { Tabs, Tab } from "react-bootstrap";
import React, { Component } from "react";

import CoinStats from "./components/coinStats";
import UpdateCoinStatsComponent from "./coinbase/wallets.js";

function App() {
  return (
    <div className="text-monospace">
      <nav className="navbar navbar-dark fixed-top bg-dark flex-md-nowrap p-0 shadow">
        <img src={logo} className="App-logo" alt="logo" height="32" />
        <b>CryptoDashboard</b>
      </nav>
      <div className="container-fluid mt-5 text-center">
        <br></br>
        <h1>CryptoBalanceDashboard</h1>
        <h2></h2>
        <br></br>
        <div className="row">
          <main role="main" className="col-lg-12 d-flex text-center">
            <div className="content mr-auto ml-auto">
              <Tabs defaultActiveKey="dashboard" id="mainTabs">
                <Tab eventKey="dashboard" title="Dashboard">
                  <div>
                    <h1>Dashboard</h1>
                  </div>

                  <div id="dashCoinTabsDiv">
                    <Tabs id="dashCoinTabs">
                      <Tab eventKey="dashboard_all" title="ALL">
                        <h2>ALL DASH</h2>
                      </Tab>
                      <Tab eventKey="dashboard_BTC" title="BTC">
                        <h2>BTC DASH</h2>
                        <CoinStats coin="BTC" id="BTC_Stats"></CoinStats>
                      </Tab>
                      <Tab eventKey="dashboard_ETH" title="ETH">
                        <h2>ETH DASH</h2>
                      </Tab>
                      <Tab eventKey="dashboard_DOGE" title="DOGE">
                        <h2>DOGE DASH</h2>
                      </Tab>
                    </Tabs>
                  </div>
                </Tab>
              </Tabs>
            </div>
          </main>
        </div>
      </div>
    </div>
  );
}

export default App;
