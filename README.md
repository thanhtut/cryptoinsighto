# Crypto Insighto 
A simulated (aka toy) datapipeline for processing real-time order book feeds from coin base and generating insights from it.

## How to test or run 
This is written in python and orgnaized as a Poetry project. 
The tests are written using pytest.

Before anything do poetry install.

Run generate data 
```
poetry run generate_mock
```

Run tests
```
poetry run pytest
```
## 1. Plan Data Feed and Product Selection

Assumption 1: The assumption is that the data is coming from GET [product book](https://docs.cdp.coinbase.com/exchange/reference/exchangerestapi_getproductbook) with Level 2 request. According to the Coinbase's documentation 

> Level 2: Full order book (aggregated) and auction info.

Assumption 2: I am not familiar with coinbase API, but seems like level 2 data is necessary to compute max-spread. Example response is 
```
{
  "bids": [
    ["71234.56", "5.67", "3"],
    ["71234.55", "2.34", "2"],
    ["71234.54", "1.11", "1"]
  ],
  "asks": [
    ["71235.57", "4.56", "2"],
    ["71235.58", "3.45", "1"],
    ["71235.59", "2.34", "1"]
  ],
  "sequence": 987654321
}
```
I will wrap this response in the following pydnatic model. 
Assumpton 3: price_level can be any non zero float and quantity has to be also non zero Decimal. The quantity in reality can have limits like Satoshi (unit) is the smallest unit of bitcoin. But simplied to any non zero Decimal for now. Number of orders is non-zero integer.

## 2. Error handling 
### 2.1 Error handling during ingest from the API
Ingesting API from a third-party source, CoinBase, requies graceful handling of common and expected errors in third-party API outages, third-party API performance degradation (very slow reponse times) and invalid/inconsistent data.

#### API outages
Tenacity python pacakge will be used to handle third-paty API outages and performance degradatoin issues. The max number of retries will be set to 5 retries with exponential wait time between each retries. The ingestion compoment will run as a Docker container and when the number of retries has been reached the container will be stop and an alert system will be set up to send emails/slacks to the team in order to notify about the crashes.

#### Data validation
Data validation will be done using Pydantic. When reading an invalid data into a Pydantic object a validation error will be raised and it will be handled and logged. Validation errors should be forwarded to another component that will compile and send a report of validation errors after every 10 validation errors. 

## 3. Design highlights
Mostly asynchronous methods since it is more CPU efficient way of handling event driven data handling code and external API calls that can have response times that are out of our control.

Configuration in environment variables (inspired by 12 factor apps)

Explicit mapping of data formats from third-party APIs to our own internal data format since we will probably want to add other third-party API sources.

Seperate decoupled components for data extraction, data loading, transforming and generating insights.

## 4. Implemented logics 
1. Highest Bid and Lowest Ask (refresh interval, every 5 mins)
2. Max Spread 
3. Mid price and forecasting