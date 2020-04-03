import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Olympic2016Rio.csv')

# Filtering first 20 countries
filtered_df = df.head(n=20)

# Removing empty spaces from State column to avoid errors
filtered_df = filtered_df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Preparing data
data = [go.Bar(x=filtered_df['NOC'], y=filtered_df['Total'])]

# Preparing layout
layout = go.Layout(title='Olympics 2016', xaxis_title="Country",
                   yaxis_title="Total Medals")


# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='olympic_barchart.html')

