from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import pandas as pd
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
russian_stop_words = stopwords.words('russian')

# Load the dataset
data = pd.read_csv('reviews.csv')

# Assuming there's a column named 'text' containing the text to cluster
# If the column has a different name, replace 'text' with the actual column name
texts = data['Text'].fillna('')  # Fill NA values with empty strings

# Preprocess and vectorize the text using TF-IDF
vectorizer = TfidfVectorizer(stop_words=russian_stop_words)
X = vectorizer.fit_transform(texts)

# Number of clusters - adjust this based on your needs
num_clusters = 3

# Perform KMeans clustering
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
kmeans.fit(X)

# Assign the cluster labels to the dataframe
data['cluster'] = kmeans.labels_

print(data)