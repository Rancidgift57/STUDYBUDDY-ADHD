import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Step 1: Create the Dataset
# Example data representing ADHD-suitable study videos
data = {
    'video_id': ['101', '102', '103', '104', '105'],
    'title': [
        'Interactive Math Concepts for Kids',
        'Quick Science Experiments for Beginners',
        'Visual History Lessons - Short & Fun',
        'Creative Writing Exercises for Engagement',
        'Basics of Geography - Interactive World Tour'
    ],
    'description': [
        'A video focusing on interactive math games to explain basic concepts.',
        'Science experiments designed to be quick and engaging for beginners.',
        'History lessons presented visually with quick summaries.',
        'Creative exercises to keep students engaged in writing.',
        'An interactive approach to learning basic geography concepts.'
    ],
    'tags': [
        'math, interactive, ADHD, kids',
        'science, experiments, ADHD, short',
        'history, visual, ADHD, fun',
        'writing, engagement, ADHD, exercises',
        'geography, interactive, ADHD, basics'
    ],
    'duration_minutes': [5, 7, 10, 8, 6],  # Short durations suited for ADHD
}

videos_df = pd.DataFrame(data)

# Step 2: Process Text Data
videos_df['content'] = videos_df['title'] + ' ' + videos_df['description'] + ' ' + videos_df['tags']
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(videos_df['content'])

# Step 3: Compute Similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Step 4: Recommendation Function
def recommend_videos(video_id, cosine_sim=cosine_sim, df=videos_df, top_n=3):
    idx = df.index[df['video_id'] == video_id].tolist()[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:top_n + 1]
    video_indices = [i[0] for i in sim_scores]
    return df.iloc[video_indices][['video_id', 'title', 'description', 'duration_minutes']]

# Step 5: Get Recommendations
video_id = '101'  # Example video ID for recommendations
recommendations = recommend_videos(video_id)
print("Recommended Videos for ADHD students:")
print(recommendations)
