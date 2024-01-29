<h1>StockSight Assistant</h1>

<p>Welcome to StockSight Assistant, your reliable stock companion powered by accurate data from the Yahoo Finance API. This tool provides users with real-time stock data and the ability to visualize price trends over the past year. Additionally, users can calculate simple moving averages for any given timeframe.</p>

<h2>Getting Started</h2>

<ol>
  <li><strong>API Key Setup:</strong> You need to obtain an API key from OpenAI. This key must be stored in a plain text file in the same directory as the main file. The name of this file should replace "api_key" in line 8 of the main file.</li>

  <li><strong>Dependencies Installation:</strong> Install the required dependencies by running:
      <pre><code>pip install -r requirements.txt</code></pre>
  </li>

  <li><strong>Running the Application:</strong> To start the application, run the following command:
      <pre><code>streamlit run main.py</code></pre>
  </li>
</ol>

<h2>Features</h2>

<ul>
  <li><strong>Accurate Stock Data:</strong> Utilizes the Yahoo Finance API to fetch precise stock data.</li>
  
  <li><strong>Price Plotting:</strong> Visualizes the price trends of a stock over the past year.</li>

  <li><strong>Simple Moving Average Calculation:</strong> Calculates simple moving averages for any given timeframe.</li>
</ul>

<h2>Important Notes</h2>

<ul>
  <li><strong>Security:</strong> Ensure that your API key is stored securely and not shared with anyone online.</li>

  <li><strong>Functionality Limitations:</strong> While the tool provides accurate stock data and basic analysis like simple moving averages, more complex calculations such as the relative strength index (RSI) may not be implemented yet.</li>
</ul>
