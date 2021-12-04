import React, { Component } from "react";

class Dashboard extends React.Component {
  state = {
    wallets: [],
  };

  render() {
    return (
      <React.Fragment>
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
              <Wallet coin="BTC"></Wallet>
            </Tab>
            <Tab eventKey="dashboard_ETH" title="ETH">
              <h2>ETH DASH</h2>
            </Tab>
            <Tab eventKey="dashboard_DOGE" title="DOGE">
              <h2>DOGE DASH</h2>
            </Tab>
          </Tabs>
        </div>
      </React.Fragment>
    );
  }
}

export default Dashboard;
