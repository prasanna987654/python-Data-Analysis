import pandas as pd
import matplotlib.pyplot as plt
ipl_df = pd.read_csv('deliveries_small.csv')
player_runs = ipl_df.groupby('batter')['total_runs'].sum()
best_players = player_runs.sort_values(ascending=False).head(10)
plt.figure(figsize=(12,7))
best_players.plot(kind='bar',color='teal')
plt.title('IPL Leaders: Top 10 Run Scorers')
plt.xlabel('Player')
plt.ylabel('Runs Scored')
plt.savefig('ipl_top_scorers_chart.png')
print("Successfully generated the IPL chart!")
