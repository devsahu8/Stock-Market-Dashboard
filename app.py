from load_df import load_df 
import streamlit as st 
from analsis import daily_return 
from analsis import Summary 
from plot import line_plot 
from plot import daily_plot 
from plot import cumm_plot 
from plot import MA_plot 
from analsis import ma 
st.title("Stock Analysis Dashboard") 
ticker = st.text_input("Ticker", "AAPL") 
start = st.date_input("Start Date") 
end = st.date_input("End Date") 
days = st.number_input("Period for SMA", min_value=1, step=1)
days = int(days)
if st.button("Run"): 
    df = load_df(ticker, start, end) 
     
    st.write(df) 
     
    stats = Summary(df) 
    df = daily_return(df)
    df=ma(df,days)

    st.write("Moving Average", df["MA"].iloc[days:])
    st.write(stats) 
    st.pyplot(MA_plot(df))
    st.pyplot(line_plot(df)) 
    st.pyplot(daily_plot(df)) 
    st.pyplot(cumm_plot(df)) 
    
    