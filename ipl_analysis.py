import pandas as pd
#1.Load your downloaded data
#Make sure deliveries.csv is in the SAME folder as this script
df = pd.read_csv('deliveries.csv')
#2.Group data by batsman and sum their runs
batsman_total = df.groupby('batter')['total_runs'].sum()
#3.Get the Top 10 scorers
top_10 = batsman_total.sort_values(ascending=False).head(10)
print("---IPL Top 10 Run Scorers(2008-2024)---")
print(top_10)
