import multiprocessing

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from nltk.corpus import stopwords
import nltk
import pandas as pd
import spacy
from joblib import dump, load

# nltk.download('stopwords')

nlp = spacy.load(
    '/Users/olga/AppData/Local/Programs/Python/Python312/Lib/site-packages/ru_core_news_sm/ru_core_news_sm-3.7.0')


def preprocess_texts(txt_chunk):
    preprocessed_texts = []
    preprocessed_labels = txt_chunk['sentiment'].tolist()

    for doc in nlp.pipe(txt_chunk["review"], disable=["parser", "ner"]):
        tokens = [token.lemma_ for token in doc if not token.is_stop]
        preprocessed_texts.append(" ".join(tokens))
    print(f"I'm done: {len(preprocessed_texts)} of preprocessed_texts, {len(preprocessed_labels)} of preprocessed_labels")

    return preprocessed_texts, preprocessed_labels


if __name__ == '__main__':
    data_size = 90000
    cores_to_use = 15  # Max for 32 CPU cores and 32 GiB RAM
    chunk_size = data_size // cores_to_use

    data = pd.read_csv("rld/reviews.csv", sep='\t', chunksize=chunk_size)

    pool = multiprocessing.Pool(processes=cores_to_use)
    results = pool.map(preprocess_texts, data)
    pool.close()
    pool.join()

    texts_preprocessed = [text for result in results for text in result[0]]
    labels = [label for result in results for label in result[1]]

    test_data = pd.read_csv("rev_test.csv")
    test_txt = test_data["Text"]
    test_labels = test_data["Label"]

    tfidf_vectorizer = TfidfVectorizer(stop_words=stopwords.words('russian'))

    texts_v = tfidf_vectorizer.fit_transform(texts_preprocessed)

    test_txt_v = tfidf_vectorizer.transform(test_txt)

    model = LogisticRegression(max_iter=1000)
    model.fit(texts_v, labels)
    # dump(model, 'ozon_model.joblib')

    y_pred = model.predict(test_txt_v)
    for pred in y_pred:
        print(pred)

    accuracy = accuracy_score(test_labels, y_pred)
    print(f"Model accuracy: {accuracy:.2f}")
