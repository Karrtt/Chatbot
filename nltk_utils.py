import nltk
#nltk.download('punkt')
from nltk.stem.porter import PorterStemmer
import numpy as np



def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stemm(word):
    stemmer = PorterStemmer()
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence, all_words):
    tokenized_sentence  = [stemm(i) for i in tokenized_sentence]

    bag =  np.zeros(len(all_words),dtype=np.float32)

    for ind,x in enumerate(all_words):
        if x in tokenized_sentence:
            bag[ind]=1
    
    return bag




