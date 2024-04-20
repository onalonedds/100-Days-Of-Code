# import spacy
# import pymorphy3
#
# # Load the Russian language model
# nlp = spacy.load('/Users/olga/AppData/Local/Programs/Python/Python312/Lib/site-packages/ru_core_news_sm/ru_core_news_sm-3.7.0')
#
# # Example of lemmatization
# doc = nlp("Эти фильмы были отличными.")
# lemmatized_text = " ".join([token.lemma_ for token in doc])
# print(lemmatized_text)
import multiprocessing

import nltk
import pandas as pd
import spacy

# nltk.download('stopwords')

nlp = spacy.load(
     '/Users/olga/AppData/Local/Programs/Python/Python312/Lib/site-packages/ru_core_news_sm/ru_core_news_sm-3.7.0')


def preprocess_texts(txt_chunk):
    preprocessed_texts = []
    for doc in nlp.pipe(txt_chunk["review"], disable=["parser", "ner"]):
        tokens = [token.lemma_ for token in doc if not token.is_stop]
        preprocessed_texts.append(" ".join(tokens))
        print("I'm working...")
    print("I'm done")
    return preprocessed_texts


if __name__ == '__main__':
    # data = pd.read_csv("rld/reviews.csv", sep='\t', chunksize=10000)
    # pool = multiprocessing.Pool(processes=9)
    # results = pool.map(preprocess_texts, data)
    # pool.close()
    # pool.join()
    #
    # print(results)
    print(int(multiprocessing.cpu_count() / 4))

