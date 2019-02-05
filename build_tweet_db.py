import sqlite3
import pandas as pd
import numpy as np
import re
conn = sqlite3.connect('tweetdatabase.db')
c = conn.cursor()
df = pd.read_csv('twitterData/cred_event_SearchTweets.data',
                delimiter = '\t', error_bad_lines=False)
df.drop(columns=['topic_key', 'ListOf_tweetid_author_createdAt_tuple'], inplace=True)
df1 = pd.read_csv('twitterData/cred_event_TurkRatings.data',
                 delimiter='\t', error_bad_lines=False)
df1.drop(0, inplace=True)
df1.Cred_Ratings = df1.Cred_Ratings.apply(lambda x: [int(i) for i in re.findall('(-?\d)', x)])
df['avg_score'] = [np.average(x) for x in df1.Cred_Ratings]
df.index.names = ['id']
df.to_sql('events', con=conn, if_exists='replace')
conn.commit()
