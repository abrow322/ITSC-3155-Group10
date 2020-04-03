import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('D:\Computer Science\Software Engineering\VisualizationLab\Software-Eng\Datasets\Weather2014-15.csv')

def getMonthlyMax(month):
    is_month = df['month'] == month
    df_month = df[is_month]
    maxTemp = max(df_month["actual_max_temp"])
    return maxTemp

def getMonthlyMin(month):
    is_month = df['month'] == month
    df_month = df[is_month]
    minTemp = min(df_month["actual_min_temp"])
    return minTemp

def getMonthlyAvg(month):
    is_month = df['month'] == month
    total = 0
    months = df[is_month]["actual_mean_temp"].values.tolist()  # Convert df to list
    for i in range(len(months)):
        total += months[i]
    average = total/len(months)
    return average

months = df["month"].values.tolist()  # Convert df to list
months = list(dict.fromkeys(months)) # Remove duplicates
print(months)

# Initialize lists
maxTempList = []
minTempList = []
avgTempList = []
for i in range(len(months)):
    maxTempList.append(getMonthlyMax(months[i]))
    minTempList.append(getMonthlyMin(months[i]))
    avgTempList.append(getMonthlyAvg(months[i]))

# Preparing Data
trace1 = go.Scatter(x=months, y=maxTempList, mode='lines', name='Max temp')
trace2 = go.Scatter(x=months, y=minTempList, mode='lines', name='Min temp')
trace3 = go.Scatter(x=months, y=avgTempList, mode='lines', name='Average temp')
data = [trace1, trace2, trace3]

# Preparing Layout
layout = go.Layout(title='Monthly weather data',
                   xaxis_title="Month", yaxis_title="Temperature")

#Plot the figure and save to HTML file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='weather_multi_linechart.html')
