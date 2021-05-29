import plotly.express as px
import pandas as pd

df = pd.read_csv('./data.csv')
fig = px.scatter(df,x='cases',y='date',color='country')
fig.show()