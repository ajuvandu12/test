import pandas as pd
df=pd.read_csv("video_game_sales11.csv")
ps4_shooter_count = df[(df['Platform'] == 'PS4') & (df['Genre'] == 'Shooter')].shape[0]
print(df[(df['Platform'] == 'PS4') & (df['Genre'] == 'Shooter')])
print(ps4_shooter_count)


nintendo_platforms = ['Wii', 'DS', '3DS', 'GBA', 'GB', 'DS', 'N64', 'NES']  # Add any other Nintendo platforms
nintendo_sales = df[(df['Platform'].isin(nintendo_platforms)) & (df['Year'] >= 2000) & (df['Year'] <= 2010)]['Global_Sales'].sum()
print(nintendo_sales)

df=df.sort_values(by="Year");
