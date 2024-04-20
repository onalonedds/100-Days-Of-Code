from transformers import AutoTokenizer, AutoModel
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import torch
import pandas as pd
import numpy as np

df = pd.read_csv('reviews_featured.csv')

combined_features = df[['p_points', 'n_points']].fillna(0).values

reviews = df['Text'].tolist()

tokenizer = AutoTokenizer.from_pretrained("DeepPavlov/rubert-base-cased")
model = AutoModel.from_pretrained("DeepPavlov/rubert-base-cased")

model.eval()


def get_embeddings(texts):
    with torch.no_grad():
        embeddings = []
        for text in texts:
            inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
            outputs = model(**inputs)
            embeddings.append(outputs.pooler_output[0].numpy())
    return np.vstack(embeddings)


embeddings = get_embeddings(reviews)

combined_features = np.concatenate([embeddings, combined_features], axis=1)

n_clusters = 3  # Adjust based on your needs
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
clusters = kmeans.fit_predict(combined_features)

print(clusters)

pca = PCA(n_components=2)
reduced_embeddings = pca.fit_transform(embeddings)

plt.figure(figsize=(10, 8))
plt.scatter(reduced_embeddings[:, 0], reduced_embeddings[:, 1], c=clusters, cmap='viridis', alpha=0.5)
plt.title('Clusters of Customer Reviews')
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.colorbar()
plt.show()