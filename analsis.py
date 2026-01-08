import pandas as pd
import numpy as np

def daily_return(df):
    df["Daily Return"]=df["Close"].pct_change()
    df["Cummulative"]=(df["Daily Return"]+1).cumprod()
    return df

def Summary(df):
    return {
    "Daily Returns->":df["Daily Return"],
    "Cummulative Returns->":df["Cummulative"]
    }

def ma(df,days):
     ma_l=[] 
     for x in range(len(df)): 
        if x<days-1: 
            ma_l.append(np.nan) 
        else: 
            ma_l.append(df["Close"].iloc[x-days+1:x+1].mean().item()) 

     df["MA"]=ma_l 
     
     return df
