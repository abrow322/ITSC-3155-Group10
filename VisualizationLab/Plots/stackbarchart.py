import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
traces = []

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Olympic2016Rio.csv')

# Removing empty spaces from NOC column to avoid errors
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Creating sum of medals
new_df = df.groupby(['NOC']).agg({'Gold': 'sum', 'Silver': 'sum', 'Bronze': 'sum', 'Total': 'sum'}).reset_index()

# Sorting values and select first 20 Countries
new_df = new_df.sort_values(by=['Total'], ascending=[False]).head(20).reset_index()

# Preparing data
trace1 = go.Bar(x=new_df['NOC'], y=new_df['Bronze'], name='Bronze', marker={'color': '#CD7F32'})
trace2 = go.Bar(x=new_df['NOC'], y=new_df['Silver'], name='Silver', marker={'color': '#9EA0A1'})
trace3 = go.Bar(x=new_df['NOC'], y=new_df['Gold'], name='Gold', marker={'color': '#FFD700'})
traces = [trace1, trace2, trace3]

# Preparing layout
layout = go.Layout(title='Total number of Gold, Silver, and Bronze metals by the 20 first top Countries',
                   xaxis_title="Country", yaxis_title="Number of Medals", barmode='stack')

# Plot the figure and saving in a html file
fig = go.Figure(data=traces, layout=layout)
pyo.plot(fig, filename='stackbarchart.html')
