import yfinance as yf
import pandas as pd

def load_df(ticker,start_date,end_date):
    df=yf.download(ticker,start_date,end_date)
    df=df[["Close","High","Low","Open","Volume"]]
    return df
