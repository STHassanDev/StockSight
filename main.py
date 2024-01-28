import json 
import openai
import pandas as pd 
import matplotlib.pyplot as plt 
import streamlit as st 
import yfinance as yf 

openai.api_key = open("secret/Key","r").read()

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

functions = [ #The list of dictionaries chat gpt will use to determine which function is needed for the given prompt.
    {
        'name':'get_stock_price',
        'description': "Retrieves the latest stock price given the ticker of a company.",
        'parameters': {
            'type': 'object',
            'properties': {
                'ticker':{
                    'type': 'string',
                    'description': 'The ticker symbol for the stock of a company (Example: NFLX for Netflix or ADBE for Adobe)'
                    }
                },
            'required': ["ticker"]
            }
        },

    {
        'name':'simple_moving_average',
        'description': "Calculates the simple moving average of stock given the ticker symbol and a window.",
        'parameters': {
            'type': 'object',
            'properties': {
                'ticker':{
                    'type': 'string',
                    'description': 'The ticker symbol for the stock of a company (Example: NFLX for Netflix or ADBE for Adobe)'
                    },
                'window':{
                    'type': 'interger',
                    'description': "The timeframe to use when finding the simple moving average."
                    }
                },
            'required': ["ticker","window"]
            }
        },

    {
        'name':'get_stock_price',
        'description': "Retrieves the latest stock price given the ticker of a company.",
        'parameters': {
            'type': 'object',
            'properties': {
                'ticker':{
                    'type': 'string',
                    'description': 'The ticker symbol for the stock of a company (Example: NFLX for Netflix or ADBE for Adobe)'
                    }
                },
            'required': ["ticker"]
            }
        }
    
]