# Quantitative-Portfolio-Analysis
Professional Python implementation for calculating and visualizing returns of a multi-asset equity portfolio.


## Project Overview

This repository demonstrates core portfolio analysis techniques used in quantitative finance and asset management:

- Historical price data collection using `yfinance`
- Price normalization (base-100 indexing)
- Daily & annualized return calculations
- Equal-weighted portfolio return computation
- Different-weighted portfolio return computation
- Clean, reproducible financial data workflow

Perfect showcase of Python skills relevant for:
- Quantitative Research
- Portfolio Management
- Risk & Performance Analysis
- Financial Data Science

## Key Features

- Modern data retrieval with `yfinance` (2025+ compatible)
- Proper handling of trading calendar & missing data
- Normalization to 100 for intuitive performance comparison
- Simple → annualized return conversion (250 trading days convention)
- Clean pandas & numpy implementation

## Portfolio Composition (example)

- Energy: BP (British Petroleum), XOM (ExxonMobil)
- Consumer Cyclical: F (Ford)
- Financials: LNC (Lincoln National)
- Technology: AAPL (Apple)

## Technologies Used

- Python 3.10+
- pandas
- numpy
- yfinance
- matplotlib


Future Improvements:

Add log returns & geometric chaining
Implement volatility & Sharpe ratio
Add covariance/correlation matrix
Portfolio optimization (Markowitz)
Factor analysis & regression
Backtesting engine with transaction costs
