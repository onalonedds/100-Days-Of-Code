import multiprocessing

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import time


def mtrain(model_name):
    new_model = model_name()
    new_model.fit(X_train_encoded, y_train)
    return new_model


# Load your dataset
data = pd.read_csv('Squirrel_Data.csv')
X = data['Primary Fur Color'].fillna('')
y = data['Location'].fillna('')

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)  # Dense output
X_train_encoded = encoder.fit_transform(X_train.values.reshape(-1, 1))
X_test_encoded = encoder.transform(X_test.values.reshape(-1, 1))

if __name__ == '__main__':

    start = time.time()

    # # Models
    # models = {
    #     'Decision Tree': DecisionTreeClassifier(),
    #     'Random Forest': RandomForestClassifier(),
    #     'Naive Bayes': GaussianNB()
    # }
    #
    # # Train the models
    # for name, model in models.items():
    #     model.fit(X_train_encoded, y_train)

    pool = multiprocessing.Pool(processes=3)
    results = pool.map(mtrain, [DecisionTreeClassifier, RandomForestClassifier, GaussianNB])
    pool.close()
    pool.join()

    # Make predictions
    for model in results:
        y_pred = model.predict(X_test_encoded)
        accuracy = accuracy_score(y_test, y_pred)
        print(f"Accuracy: {accuracy:.3f}")

    print(f'Time spent: {time.time() - start}')
