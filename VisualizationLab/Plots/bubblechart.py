import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Weather2014-15.csv')

# Average min and max for all days in each month...
# Accumulate min and max value for all days per month, then divide by number of days
# df['Unrecovered'] = df['Confirmed'] - df['Deaths'] - df['Recovered']

# Preparing data
data = [
    go.Scatter(x=df['month'],
               y=df['average_max_temp'],
               text=df['month'],
               mode='markers',
               marker=dict(size=df['average_min_temp']
                           , color=df['average_min_temp'], showscale=True))
]

# Preparing layout
layout = go.Layout(title='Average Min and Max Temperatures Each Month', xaxis_title="Month",
                   yaxis_title="Average Max", hovermode='closest')

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bubblechart.html')