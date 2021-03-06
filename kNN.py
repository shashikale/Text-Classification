from ReadPreprocessData import read_preprocess
from Tokenize import tokenize
from SharedFunctions import get_current_time, fmt, find_accuracy

from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import numpy as np
import gc

from datetime import datetime

# reading and preprocessing data
t = get_current_time()
train_features, train_labels, test_features, test_labels = read_preprocess()
print("Time taken to Read and Preprocess Raw Data:", datetime.strptime(get_current_time(), fmt) - datetime.strptime(t, fmt))

# vectorizing data
t = get_current_time()
vectorizer = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
train_features = vectorizer.fit_transform(train_features)
test_features = vectorizer.transform(test_features)
print("Time taken to Vectorize:", datetime.strptime(get_current_time(), fmt) - datetime.strptime(t, fmt))

# training
t = get_current_time()
classifier = KNeighborsClassifier(n_neighbors=3, weights='uniform', algorithm='auto', p=1,
                                  metric='minkowski', n_jobs=-1)
classifier.fit(train_features, train_labels)
print("Time taken to Fit:", datetime.strptime(get_current_time(), fmt) - datetime.strptime(t, fmt))

# fitting
t = get_current_time()
predicted_labels = classifier.predict(test_features)
print("Time taken to Predict:", datetime.strptime(get_current_time(), fmt) - datetime.strptime(t, fmt))

# finding Accuracy
find_accuracy(predicted_labels, test_labels)
