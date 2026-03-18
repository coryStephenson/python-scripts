# Install
!pip install pycoingecko

# Import library
from pycoingecko import CoinGeckoAPI

# Create client object
cg = CoinGeckoAPI()

# Employ a function to request data 
# The response is a JSON file expressed as a Python dictionary of nested lists
# that includes price, market cap, and total volumes
# which contain the UNIX timestamp and the price at that time
bitcoin_data = cg.get_coin_market_chart_by_id(id = 'bitcoin', vs_currency = 'usd', days = 30)

# Select price using the 'prices' key
data = pd.DataFrame(bitcoin_data['prices'], columns=['TimeStamp', 'Price'])

# Convert the UNIX timestamp to a more readable format
# The input is the 'TimeStamp' column
# We append the output to the new column, 'Date'
data['Date'] = pd.to_datetime(data['TimeStamp'], unit = 'ms')

# Get data for daily candlesticks, grouping by date
candlestick_data = data.groupby(data.Date.dt.date).agg({'Price': ['min', 'max', 'first', 'last']})

# Create candlestick chart
import plotly.graph_objects as go
import plotlyfig = go.Figure(data=[go.Candlestick(x = candlestick_data.index, 
                                                  open = candlestick_data['Price']['first'],
                                                  high = candlestick_data['Price']['max'],
                                                  low = candlestick_data['Price']['min'],
                                                  close = candlestick_data['Price']['last']
                                   )
                   ])
fig.update_layout(xaxis_rangeslider_visible = False, xaxis_title = 'Date',
yaxis_title = 'Price (USD $)', title = 'Bitcoin Candlestick Chart Over Past 30 Days')

# Plot candlestick chart
plotly.offline.plot(fig, filename = './bitcoin_candlestick_graph.html', auto_open=False)
