import pandas as pd
import re

#path to file locations from Paperspace
df = pd.read_csv('/storage/cred_event_SearchTweets.data',
                delimiter = '\t', error_bad_lines=False)


df.ListOf_tweetid_author_createdAt_tuple = df.ListOf_tweetid_author_createdAt_tuple.apply(
    lambda x: re.findall('(\({1}.*?\))', x))

# for i, val in enumerate(df.ListOf_tweetid_author_createdAt_tuple):
#     df.ListOf_tweetid_author_createdAt_tuple.iloc[i] = [re.findall('(?<=\')([^\,]*?)(?=\')', x)
#     for x in val]

new_rows = []
for x in df.ListOf_tweetid_author_createdAt_tuple:
    new = [re.findall('(?<=\')([^\,]*?)(?=\')', i)for i in x]
    new_rows.append(new)
df.ListOf_tweetid_author_createdAt_tuple = new_rows


topics_length = len(df)
rows_list = []
for i in range(topics_length):
    tweets = df.ListOf_tweetid_author_createdAt_tuple.iloc[i]
    for tweet in tweets:
        tweet_dict = {'tweet_id': tweet[0][3:], 'author': tweet[1][7:],
        'date': tweet[2][10:], 'topic_id': i}
        rows_list.append(tweet_dict)

tweet_df = pd.DataFrame(rows_list)

tweet_df.to_csv('/storage/tweet_df_final.csv')
