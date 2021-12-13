import React, { Component } from "react";
import { Tabs, Tab } from "react-bootstrap";
import PriceWidget from "./priceWidget";

import "bootstrap/dist/css/bootstrap.css";
// Component to hold individual coin statistics

class Wallet extends React.Component {
  colours = {
    BTC: "orange",
    ETH: "blue",
    DOGE: "#cca737",
    ALL: "black",
    Total: "black",
  };

  render() {
    //console.log("Creating wallet: State: ", this.state, "Props: ", this.props);

    if (this.props.wallet.coin != "ALL") {
      return (
        <React.Fragment>
          <div>
            <h2>
              Balance:{" "}
              {this.props.wallet.balance + " " + this.props.wallet.coin}{" "}
            </h2>

            <h2 style={{ color: "green" }}>
              High:
              {Object.values(this.props.wallet.dateCumlBalUSDSparse).pop()[0]}
            </h2>
            <h2 style={{ color: "red" }}>
              Low:
              {Object.values(this.props.wallet.dateCumlBalUSDSparse).pop()[1]}
            </h2>
          </div>
          <PriceWidget coin={this.props.wallet.coin} fullGraph={true} />
        </React.Fragment>
      );
    } else {
      return (
        <React.Fragment>
          <div>
            <table className="table m-2">
              <tbody>
                <tr className="m-2">
                  {this.props.wallet.tableHeaders.map((col) => {
                    return (
                      <td>
                        <h2 style={{ color: this.colours[col] }}> {col}</h2>
                      </td>
                    );
                  })}
                </tr>

                <tr>
                  {this.props.wallet.balanceRow.map((col) => {
                    return (
                      <td>
                        <h2> {col} </h2>
                      </td>
                    );
                  })}
                </tr>
                <tr>
                  {this.props.wallet.balanceUsdHighRow.map((col) => {
                    return (
                      <td>
                        <h2 style={{ color: "green" }}>$ {col}</h2>
                      </td>
                    );
                  })}
                </tr>
                <tr>
                  {this.props.wallet.balanceUsdLowRow.map((col) => {
                    return (
                      <td>
                        <h2 style={{ color: "red" }}>$ {col}</h2>
                      </td>
                    );
                  })}
                </tr>
              </tbody>
            </table>
          </div>

          <div className="row">
            {this.props.wallet.allCoins.map((coin) => {
              return (
                <div className="col col-sm">
                  <PriceWidget coin={coin} fullGraph={false} />{" "}
                </div>
              );
            })}
          </div>
        </React.Fragment>
      );
    }
  }
}

export default Wallet;

{
  /* <div>
            <h2>Balance: {this.props.wallet.balance + " "} </h2>
            <h2 style={{ color: "green" }}>
              High: {this.props.wallet.allUsdStrHigh}
            </h2>
            <h2 style={{ color: "red" }}>
              Low:
              {this.props.wallet.allUsdStrLow}
            </h2>
          </div> */
}
