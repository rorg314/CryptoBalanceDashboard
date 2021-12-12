# Crypto Balance Dashboard

This is a prototype for a React based crypto balances dashboard application.

The application uses a Python back-end to process Coinbase reports which are then fetched by the React frontend dashboard.

# Python Backend

The back-end used to process Coinbase report data is implemented in Python and contains a small Flask application that works as a basic API for the react front-end. The back-end processes all of the information in the report and produces an appropriate json representation of the desired data.

Currently, reports are not fetched using the Coinbase API but must be uploaded by the user. The rest is handled automatically using the Coinbase API to fetch price data etc.

# React Frontend

The frontend is created with node/react. This simply fetches the .json data generated from the back-end and displays the information appropriately. All calculations are done on the back-end to minimise the processing (headaches) through JavaScript.

# Installation

This application requires Python and Node.js to run

- Python (Latest version is ok) [python.org/downloads/](https://www.python.org/downloads/)

- Node.js (v14.17.0, but latest likely ok) [nodejs.org/en/](https://nodejs.org/en/)

## Python backend

To install the backend navigate into the [CoinbaseProcessing](./CoinbaseProcessing) folder.

Create a python virtual environment

```
python -m venv env
```

Then activate it with the appropriate script (cmd or powershell)

```
cmd: env/Scripts/activate.bat

powershell: env/Scripts/activate.ps1
```

Then install the required packages

```
pip install -r requirements.txt
```

Once the packages have installed, the backend server can be started by running the flask application [app.py](./app.py) using

```
flask run
```

within this folder.

Or alternatively, by launching with the included debug configuration

## Node/React frontend

Navigate into the [CryptoDashboardApp](./CryptoDashboardApp) folder

```
cd cryptodashboardapp
```

Install the required node packages

```
npm install
```

Run the front-end server using

```
npm start
```

within the [CryptoDashboardApp](./CryptoDashboardApp) folder

## Coinbase Report

This is the only input data required by the user. Future iterations will be able to get this using the coinbase API when given authentication from the users API key.

Download a Coinbase report from your profile, save it as a .csv file named `Report.csv` in the [CryptoDashboardApp](./CryptoDashboardApp) folder. This will be processed by the back-end when queried by the API.

# Dashboard

Head to [localhost:3000/](http://localhost:3000/) to view the dashboard application. This will query the flask back-end (running at [localhost:5000/](http://localhost:5000/)) and display the wallet information on the dashboard, shown below.
