import pandas as pd
import numpy as np
import sqlite3


np.random.seed(42)
num_users = 10000
user_ids = [f'U{i:04d}' for i in range(1, num_users + 1)]
groups = np.random.choice(['A', 'B'], num_users, p=[0.5, 0.5])
join_dates = pd.to_datetime('2025-01-01') + pd.to_timedelta(np.random.randint(0, 30, num_users), unit='D')

users_data = pd.DataFrame({
    'user_id': user_ids,
    'test_group': groups,
    'join_date': join_dates
})


num_events = 50000
event_user_ids = np.random.choice(user_ids, num_events)


event_types = np.random.choice(['view', 'click', 'view'], num_events, 
                               p=[0.75, 0.15, 0.10]) # Baseline
for i in range(num_events):
    if users_data[users_data['user_id'] == event_user_ids[i]]['test_group'].iloc[0] == 'B':

        event_types[i] = np.random.choice(['view', 'click', 'view'], 1, p=[0.7, 0.2, 0.1])[0]

event_dates = pd.to_datetime('2025-01-01') + pd.to_timedelta(np.random.randint(1, 40, num_events), unit='D')

events_data = pd.DataFrame({
    'event_id': range(1, num_events + 1),
    'user_id': event_user_ids,
    'event_type': event_types, 
    'event_date': event_dates
})

conn = sqlite3.connect('ab_testing.db')

users_data.to_sql('users', conn, if_exists='replace', index=False)
events_data.to_sql('events', conn, if_exists='replace', index=False)

conn.close()

