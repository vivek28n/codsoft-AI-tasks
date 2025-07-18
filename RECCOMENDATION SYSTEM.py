import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample movie dataset (you can expand this with more movies)
data = {
    'title': [
        'Inception', 'Interstellar', 'The Dark Knight', 'The Prestige',
        'Titanic', 'Avatar', 'The Matrix', 'Shutter Island'
    ],
    'description': [
        'A thief who steals corporate secrets through the use of dream-sharing technology.',
        'A team of explorers travel through a wormhole in space in an attempt to ensure humanity\'s survival.',
        'Batman raises the stakes in his war on crime.',
        'Two stage magicians engage in a competitive rivalry.',
        'A young couple fall in love on the ill-fated Titanic.',
        'A marine on an alien planet becomes torn between two worlds.',
        'A computer hacker learns the true nature of his reality and his role in the war.',
        'A US Marshal investigates the disappearance of a murderer from a hospital for the criminally insane.'
    ]
}

# Load into a DataFrame
df = pd.DataFrame(data)

# Convert descriptions to TF-IDF vectors
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['description'])

# Compute cosine similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Function to recommend movies
def recommend_movie(title):
    if title not in df['title'].values:
        return f"Movie '{title}' not found in the database."
    
    idx = df[df['title'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:4]  # Top 3
    movie_indices = [i[0] for i in sim_scores]

    return df['title'].iloc[movie_indices].tolist()

# Example usage
user_input = input("Enter a movie you like: ")
recommendations = recommend_movie(user_input)
print("Recommended Movies:")
for movie in recommendations:
    print("- " + movie)
