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
    plt.title(f'{ticker} Stock Price Over the Last Year')
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
        'description': "Calculates the simple moving average of stock given the ticker symbol and a .",
        'parameters': {
            'type': 'object',
            'properties': {
                'ticker':{
                    'type': 'string',
                    'description': 'The ticker symbol for the stock of a company (Example: NFLX for Netflix or ADBE for Adobe)'
                    },
                'time':{
                    'type': 'integer',
                    'description': "The timeframe to use when finding the simple moving average."
                    }
                },
            'required': ["ticker","time"]
            }
        },

    {
        'name':'plot_stock_price',
        'description': "Plots the stock price for the last year when given the ticker symbol of a company.",
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

available_funcs = {
    'get_stock_price': get_stock_price,
    'simple_moving_average': simple_moving_average,
    'plot_stock_price': plot_stock_price
}

if 'messages' not in st.session_state:
    st.session_state['messages'] = []

st.title("Stock Sight Chat Bot")

prompt = st.text_input("Your input:")

if prompt:
    try:
        st.session_state['messages'].append({'role':'user','content':f'{prompt}'})

        response = openai.ChatCompletion.create(
            model = 'gpt-3.5-turbo-0613',
            messages = st.session_state['messages'],
            functions=functions,
            function_call='auto'
        )

        response_message = response['choices'][0]['message']

        if response_message.get('function_call'):
            function_name = response_message['function_call']['name']
            function_args = json.loads(response_message['function_call']['arguments'])
            if function_name in ['get_stock_price','plot_stock_price']:
                args_dict = {'ticker':function_args.get('ticker')}
            elif function_name in ['simple_moving_average']:
                args_dict = {'ticker':function_args.get('ticker'), 'window':function_args.get('window')}

            function_to_call = available_funcs[function_name]
            function_response = function_to_call(**args_dict)

            if function_name == 'plot_stock_price':
                st.image('stock.png')
            else:
                st.session_state['messages'].append(response_message)
                st.session_state['messages'].append({
                    'role':'function',
                    'name':function_name,
                    'content': function_response
                })

                second_response = openai.ChatCompletion.create(
                    model = 'gpt-3.5-turbo-0613',
                    messages = st.session_state['messages']
                    )
                st.text(second_response['choices'][0]['message']['content'])
                st.session_state['messages'].append({'role': 'assistant','content': second_response['choices'][0]['message']['content']})
        else:
            st.text(response_message['content'])         
            st.session_state['messages'].append({'role': 'assistant','content': response_message['content']})
    except Exception as e:
        raise e