import json 
import openai
import pandas as pd 
import matplotlib.pyplot as plt 
import streamlit as st 
import yfinance as yf 

def get_stock_price(ticker): # Will be used when the prompt demands the stock price of a certain company
    return str(yf.Ticker(ticker).history(period='1y').iloc[-1].Close)

