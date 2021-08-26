import re
import string
from sklearn.base import BaseEstimator, TransformerMixin

# punctuation table
table = str.maketrans('', '', string.punctuation)

class Preprocessor(BaseEstimator, TransformerMixin):

    def remove_user_names(self, s):
        return re.sub('@[^\s]+','',s)

    def remove_numbers(self, s):
        return re.sub('[0-9]','',s)

    def remove_punctuation(self, s):
        res = [w.translate(table) for w in s.split()]
        return " ".join(res)

    def n_stemmer(self, s, n):
        if(n>0):
            res = [x[:n] for x in s.split()]
            return " ".join(res)
        raise Exception("n must be a positive integer!")

    def pre_process(self, s, n=10):
        return self.n_stemmer(self.remove_punctuation(self.remove_numbers(self.remove_user_names(s.lower()))), n)

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        
        # if used for testing
        if (isinstance(X, list)):
            return [self.pre_process(x) for x in X]
        else:
            return X.apply(lambda x: self.pre_process(x))

    def __init__(self):
        return