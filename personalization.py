import pandas as pd
import numpy as np

comments_df = pd.read_csv('comments.csv')
post_performance_df = pd.read_csv('post_performance.csv')

comments_df.head()

post_performance_df.head()

comments_df.info()
print('_--------------------------')
print(post_performance_df.info())

comments_df.isna().sum()

print(post_performance_df.isna().sum())

comments_df=comments_df.drop('attachment',axis=1)
comments_df=comments_df.drop('commentId',axis=1)
post_performance_df=post_performance_df.drop('not_status',axis=1)

comments_df.isna().sum()

comments_df['Comment'] = comments_df['Comment'].fillna('Unknown')

post_performance_df.isna().sum()

comments_df['Comment']


non_numeric_ids = comments_df[~comments_df['id'].str.isnumeric()]
print("Non-numeric user_ids:\n", non_numeric_ids)


comments_df = comments_df[comments_df['id'].str.isnumeric()]


comments_df['id'] = comments_df['id'].astype(int)

merged_df = pd.merge(comments_df, post_performance_df, on='id', how='inner')
merged_df
merged_df.info()

from sklearn.metrics.pairwise import cosine_similarity
from collections import defaultdict


merged_df['Reaction'] = merged_df['liked'] = 1
merged_df

merged_df.drop(['date_x','date_y','type'], axis=1, inplace=True)
merged_df

def create_user_item_matrix(merged_df):
    matrix = pd.pivot_table(merged_df, values='Reaction', index='UID', columns='PID', aggfunc='first')
    return matrix.fillna(0)

def user_user_cf(merged_df, user_item_matrix, target_user, n_similar_users=5, n_recommendations=10):
    user_similarity = cosine_similarity(user_item_matrix)
    user_index = user_item_matrix.index.get_loc(target_user)
    similar_users = np.argsort(user_similarity[user_index])[::-1][1:n_similar_users+1]

    recommendations = defaultdict(float)
    for user in similar_users:
        user_reactions = merged_df[merged_df['UID'] == user_item_matrix.index[user]]
        for _, row in user_reactions.iterrows():
            if row['PID'] not in user_item_matrix.loc[target_user]:
                recommendations[row['PID']] += user_similarity[user_index, user] * row['Reaction']

    sorted_recommendations = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)[:n_recommendations]
    return [pid for pid, _ in sorted_recommendations]

def get_user_interests(merged_df, target_user):
    user_reactions = merged_df[merged_df['UID'] == target_user]
    return user_reactions['PID'].tolist()

def content_based_recommendation(merged_df, target_user, n_recommendations=10):
    user_interests = get_user_interests(merged_df, target_user)
    if not user_interests:
        return []

    product_co_occurrence = merged_df.groupby('UID')['PID'].apply(list).reset_index()
    product_co_occurrence['PID'] = product_co_occurrence['PID'].apply(set)

    recommendations = defaultdict(int)
    for _, row in product_co_occurrence.iterrows():
        if set(user_interests) & row['PID']:
            for product in row['PID']:
                if product not in user_interests:
                    recommendations[product] += 1

    sorted_recommendations = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)[:n_recommendations]
    return [pid for pid, _ in sorted_recommendations]

def hybrid_recommendation(df, user_item_matrix, target_user, weight_cf=0.7, weight_content=0.3, n_recommendations=10):
    cf_recommendations = user_user_cf(merged_df, user_item_matrix, target_user, n_recommendations=n_recommendations)
    content_recommendations = content_based_recommendation(merged_df, target_user, n_recommendations=n_recommendations)

    hybrid_scores = defaultdict(float)
    for pid in set(cf_recommendations + content_recommendations):
        if pid in cf_recommendations:
            hybrid_scores[pid] += weight_cf * (n_recommendations - cf_recommendations.index(pid))
        if pid in content_recommendations:
            hybrid_scores[pid] += weight_content * (n_recommendations - content_recommendations.index(pid))

    sorted_recommendations = sorted(hybrid_scores.items(), key=lambda x: x[1], reverse=True)[:n_recommendations]
    return [pid for pid, _ in sorted_recommendations]
