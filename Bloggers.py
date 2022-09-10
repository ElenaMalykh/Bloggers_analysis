import pandas as pd
from helper_function.helper_function import *

# загружаем датасет
df = pd.read_csv('static/Bloggers.csv')

# print (df.columns)
# print(df[["channel", "code_creation_date"]])

# print(df["channel"].unique())

# 'telegram_bloggers' 'instagram_bloggers' 'youtube_bloggers'
 # 'tiktok_bloggers' 'twitter_bloggers' 'facebook_bloggers'
 # 'twitch_bloggers' 'vk_bloggers'

channels=df["channel"].unique()
profit_per_channel=dict.fromkeys(channels, 0)

# for _, row in df.iterrows():
#     channel = row['channel']
#     profit = row['profit_actual_by_paid'].replace(',', '')
#     profit_per_channel[channel] += int(profit)


# print(profit_per_channel)




channels = df["channel"].unique()


average_percentage = {channel: [] for channel in channels}

for _, row in df.iterrows():
    channel = row['channel']
    float_value = get_float_from_percent(row['ROAS'])
    average_percentage[channel].append(float_value)

# for key, value in average_percentage.items():
#     print(f'{key} - {value}')

average_percentage_df = pd.DataFrame.from_dict(
    data=average_percentage,
    orient='index').transpose()
# print(average_percentage_df)



for column_name, column_value in average_percentage_df.iteritems():
    print(column_name)
    print('...........')
    print(f'mean - {column_value.mean()}')
    print(f'median - {column_value.median()}')
    print('...........\n')