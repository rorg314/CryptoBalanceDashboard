import React, { Component } from "react";

// React component for displaying price graph widget (from https://coinlib.io/widgets)

class PriceGraphWidget extends React.Component {
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

    if (this.props.fullGraph == true) {
      return (
        <div
          style={{
            height: "560px",
            backgroundColor: "#FFFFFF",
            overflow: "hidden",
            boxSizing: "borderBox",
            border: "1px solid #F0F0F0",
            borderRadius: "4px",
            textAlign: "right",
            lineHeight: "14px",
            fontSize: "12px",
            fontFeatureSettings: "normal",
            textSizeAdjust: "100%",
            boxShadow: "inset 0 -20px 0 0 #F0F0F0",
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
              style={{
                border: 0,
                margin: 0,
                padding: 0,
                lineHeight: "14px",
              }}
            ></iframe>
          </div>
          <div
            style={{
              color: "#FFFFFF",
              lineHeight: "14px",
              fontWeight: "400",
              fontSize: "11px",
              boxSizing: "borderBox",
              padding: "2px 6px",
              width: "100%",
              fontFamily: "Verdana, Tahoma, Arial, sans-serif",
            }}
          >
            <a
              href="https://coinlib.io"
              target="_blank"
              style={{
                fontWeight: 500,
                color: "#FFFFFF",
                textDecoration: "none",
                fontSize: "11px",
              }}
            >
              Cryptocurrency Prices
            </a>
            &nbsp;by Coinlib
          </div>
        </div>
      );
    } else {
      return (
        <div
          style={{
            width: "100%",
            height: "220px",
            backgroundColor: "#FFFFFF",
            overflow: "hidden",
            boxSizing: "borderBox",
            border: "1px solid #F0F0F0",
            borderRadius: "4px",
            textAlign: "right",
            lineHeight: "14px",
            blockSize: "100%",
            fontSize: "12px",
            fontFeatureSettings: "normal",
            textSizeAdjust: "100%",
            boxShadow: "inset 0 -20px 0 0 #F0F0F0",
            padding: "0px",
            margin: "0px",
          }}
        >
          <div
            style={{
              height: "200px",
              padding: "0px",
              margin: "0px",
              width: "100%",
            }}
          >
            <iframe
              src={
                "https://widget.coinlib.io/widget?type=single_v2&theme=light&coin_id=" +
                id +
                "&pref_coin_id=1505"
              }
              width="100%"
              height="196px"
              scrolling="auto"
              marginwidth="0"
              marginheight="0"
              frameborder="0"
              border="0"
              style={{
                border: "0",
                margin: "0",
                padding: "0",
                lineHeight: "14px",
              }}
            ></iframe>
          </div>
          <div
            style={{
              color: "#FFFFFF",
              lineHeight: "14px",
              fontWeight: "400",
              fontSize: "11px",
              boxSizing: "borderBox",
              padding: "2px 6px",
              width: "100%",
              fontFamily: "Verdana, Tahoma, Arial, sans-serif",
            }}
          >
            <a
              href="https://coinlib.io"
              target="_blank"
              style={{
                fontWeight: "500",
                color: "#FFFFFF",
                textDecoration: "none",
                fontSize: "11px",
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
}

export default PriceGraphWidget;
