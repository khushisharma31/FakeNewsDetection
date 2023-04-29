import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.svm import LinearSVC #a classifier that works best for text data

data = pd.read_csv("/Users/khushisharma/Desktop/NuacemAI/FakeNewsFlask/data/news_dataset.csv")
data['fake'] = data['label'].apply(lambda x: 0 if x == "REAL" else 1)
x, y = data['text'], data['fake'] 
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2) #20% of the data should be used for evaluation and 80% for training
vectorizer = TfidfVectorizer(stop_words="english", max_df=0.7)
x_train_vectorized = vectorizer.fit_transform(x_train.astype('U'))
x_test_vectorized = vectorizer.transform(x_test.astype('U'))

clf = LinearSVC()
clf.fit(x_train_vectorized, y_train)

def detectFake(text):
    vectorized_text = vectorizer.transform([text])
    if (clf.predict(vectorized_text)) == 1:
        return "Fake"
    else:
        return "Real"






