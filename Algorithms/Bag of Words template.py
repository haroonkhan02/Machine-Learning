

import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np

dataset = pd.read_csv('Restaurant_Reviews.tsv', delimiter = '\t', quoting = 3)

#cleaning the text
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

    #corpus is generally a list of words of same types
corpus = []
for i in range(0,1000):
    review = re.sub('[^a-zA-Z]', ' ' , dataset['Review'][i])
    review = review.lower()
    review = review.split() 

    # stemmer changes words to origin form like 'loved' to 'love'
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in stopwords.words('english')]
    # 'english' is added as we are dealing with eng text
    # after 'if not' conditon means that if the word defined before 'for' is not in stopwords then keep it
    # the first 'word' is that contains refined letters , the second is like 'i' in for loop, and the third is the same as first
    
    review = ' '.join(review)
    corpus.append(review)


#creating the bag of words
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
X = cv.fit_transform(corpus).toarray() 
y = dataset.iloc[:, 1].values


# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)


# Fitting classifier to the Training set
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train,y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
