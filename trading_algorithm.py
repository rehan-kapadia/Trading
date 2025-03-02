
# Trading Algorithm
import pandas as pd
import numpy as np

def analyze_trading_data(data):
    '''
    Analyze trading data for potential buy/sell signals
    '''
    # Sample implementation
    data['SMA_20'] = data['close'].rolling(window=20).mean()
    data['SMA_50'] = data['close'].rolling(window=50).mean()
    
    # Generate buy/sell signals
    data['signal'] = 0
    data.loc[data['SMA_20'] > data['SMA_50'], 'signal'] = 1  # Buy signal
    data.loc[data['SMA_20'] < data['SMA_50'], 'signal'] = -1  # Sell signal
    
    return data

def backtest_strategy(data):
    '''
    Simple backtesting function for the trading strategy
    '''
    # Initialize positions and portfolio value
    data['position'] = data['signal'].shift(1)
    data['returns'] = data['close'].pct_change()
    data['strategy_returns'] = data['position'] * data['returns']
    
    # Calculate cumulative returns
    data['cumulative_returns'] = (1 + data['returns']).cumprod()
    data['strategy_cumulative_returns'] = (1 + data['strategy_returns']).cumprod()
    
    return data
