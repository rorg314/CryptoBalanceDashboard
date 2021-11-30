

const config = require('./config.js')
const coinbase = require('coinbase')
var Client = require('coinbase').Client;

var crypto = require('crypto');

var request = require('request');

const apiKey = config.default.COINBASE_API_KEY
const apiSecret = config.default.COINBASE_API_SECRET
const userID = config.default.COINBASE_ID

const client = coinbase.Client({'apiKey':apiKey, 'apiSecret':apiSecret})


function GetTransactions(){
    //get unix time in seconds
    var timestamp = Math.floor(Date.now() / 1000);

    // set the parameter for the request message
    var req = {
        method: 'GET',
        path: 'v2/accounts/:' + String(userID) +'/buys',
        body: ''
    };

    var message = timestamp + req.method + req.path + req.body;
    console.log(message);

    //create a hexedecimal encoded SHA256 signature of the message
    var signature = crypto.createHmac("sha256", apiSecret).update(message).digest("hex");

    //create the request options object
    var options = {
        baseUrl: 'https://api.coinbase.com/',
        url: req.path,
        method: req.method,
        headers: {
            'CB-ACCESS-SIGN': signature,
            'CB-ACCESS-TIMESTAMP': timestamp,
            'CB-ACCESS-KEY': apiKey,
            
        }
    };
    
    request(options,function(err, response){
        if (err) console.log("Error!" + err);
        
        var res = response;
        console.log(response.body);
        debugger;
        
    });
    
}

export default GetTransactions;