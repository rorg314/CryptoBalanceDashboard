import React, { Component } from "react";

class PriceWidget extends React.Component {
  // Coin IDs for coinlib price widgets
  coinIds = {
    BTC: "859",
    ETH: "145",
    DOGE: "280",
  };

  render() {
    // Default to bitcoin
    var id = "859";

    if (this.props.coin in this.coinIds) {
      var id = this.coinIds[this.props.coin];
    }

    return (
      <div
        style={{
          height: "560px",
          "background-color": "#FFFFFF",
          overflow: "hidden",
          "box-sizing": "border-box",
          border: "1px solid #56667F",
          "border-radius": "4px",
          "text-align": "right",
          "line-height": "14px",
          "font-size": "12px",
          "font-feature-settings": "normal",
          "text-size-adjust": "100%",
          "box-shadow": "inset 0 -20px 0 0 #56667F",
          padding: "1px",
          padding: "0px",
          margin: "0px",
          width: "100%",
        }}
      >
        <div
          style={{
            height: "540px",
            padding: "0px",
            margin: "0px",
            width: "100%",
          }}
        >
          <iframe
            src={
              "https://widget.coinlib.io/widget?type=chart&theme=light&coin_id=" +
              id +
              "&pref_coin_id=1505"
            }
            width="100%"
            height="536px"
            scrolling="auto"
            marginwidth="0"
            marginheight="0"
            frameborder="0"
            border="0"
            style={{ border: 0, margin: 0, padding: 0, "line-height": "14px" }}
          ></iframe>
        </div>
        <div
          style={{
            color: "#FFFFFF",
            lineHeight: "14px",
            fontWeight: "400",
            fontSize: "11px",
            boxSizing: "border-box",
            padding: "2px 6px",
            width: "100%",
            fontFamily: "Verdana, Tahoma, Arial, sans-serif",
          }}
        >
          <a
            href="https://coinlib.io"
            target="_blank"
            style={{
              "font-weight": 500,
              color: "#FFFFFF",
              "text-decoration": "none",
              "font-size": "11px",
            }}
          >
            Cryptocurrency Prices
          </a>
          &nbsp;by Coinlib
        </div>
      </div>
    );
  }
}

export default PriceWidget;
