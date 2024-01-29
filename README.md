<h1>StockSight Assistant</h1>

<p>Welcome to StockSight Assistant, a powerful tool for accessing accurate stock data from Yahoo Finance API and visualizing it using Streamlit. This project allows you to retrieve stock information and plot stock prices for the past year with ease.</p>

<h2>Setup Instructions</h2>

<ol>
<li><strong>Python Environment:</strong> Make sure you have Python installed on your system. You can download it from <a href="https://www.python.org/downloads/">here</a>.</li>
<li><strong>Required Libraries:</strong> Install the necessary libraries by running:<br>
<code>pip install -r requirements.txt</code></li>
<li><strong>API Key:</strong> You need to obtain an API key from OpenAI for accessing their services. This key should be kept secure and not shared online. Create a plain text file (e.g., <code>openai_api_key</code>) containing your API key. Place this file in the same directory as the main Python file. The API key file should contain only the key without any additional text.</li>
</ol>

<h2>Usage</h2>

<p>To run the StockSight Assistant, execute the following command:</p>
<code>streamlit run main.py</code>
<p>This will launch the Streamlit application in your default web browser.</p>

<h3>Note</h3>

<p>Ensure that the file containing your OpenAI API key is named appropriately and placed in the correct directory. The name of this file should replace "api_key" in line 8 of the main Python file (<code>main.py</code>).</p>

<p><strong>Caution:</strong> Do not share your API key with anyone online.</p>
