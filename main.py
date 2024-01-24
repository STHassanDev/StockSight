import json 
import openai
import pandas as pd 
import matplotlib.pyplot as plt 
import streamlit as st 
import yfinance as yf 

def get_stock_price(ticker): # Will be used when the prompt demands the stock price of a certain company
    return str(yf.Ticker(ticker).history(period='1y').iloc[-1].Close)

def simple_moving_average(ticker,time):
    price = yf.Ticker(ticker).history(period='1y').Close
    return str(price.rolling(window=time).mean().iloc[-1])

def plot_stock_price(ticker):
    data = yf.Ticker(ticker).history(period='1y')
    plt.figure(figsize=(10,5))
    plt.plot(data.index,data.Close)
    plt.title('{ticker} Stock Price Over the Last Year')
    plt.xlabel("Date")
    plt.ylabel("Stock Price ($)")
    plt.grid(True)
    plt.savefig("stock.png")
    plt.close()