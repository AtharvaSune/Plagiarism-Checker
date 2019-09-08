import re
import os
import nltk
from data import get_files
from nltk.corpus import stopwords, wordnet
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# global variables
stop_words = set(stopwords.words('english'))

class Process():
    """
        Class with methods for preprocessing the text
        Methods:
            remove_stopwords: removes stopwords from the text
            lemmatize: implements lemmatization over the complete text
            get_wordnet_pos: generate POS tag for words in text
    """
    def __init__(self, filepath):
        """
            params: 
                filepath: path to file which has to be preprocessed
        """
        self.filename = os.path.splitext(os.path.basename(filepath))[0]
        self.filedata = open(filepath, encoding='utf-8').read()

    def get_wordnet_pos(self, word):
        """Generated POS tag for the words in a format accepted by lemmatize() function"""
        tag = nltk.pos_tag([word])[0][1][0].upper()
        tag_dict = {"J": wordnet.ADJ,
                    "N": wordnet.NOUN,
                    "V": wordnet.VERB,
                    "R": wordnet.ADV}
        return tag_dict.get(tag, wordnet.NOUN)
    
    def lemmatization(self):
        lemmatizer = WordNetLemmatizer()
        self.filedata = [lemmatizer.lemmatize(w, self.get_wordnet_pos(w)) for w in nltk.word_tokenize(''.join(self.filedata))]

    def remove_stopwords(self):
        """
            Removes stopwords from the corpus
        """
        file = []
        for i in self.filedata:
            if i.lower() not in stop_words:
                file.append(i)
        self.filedata = ' '.join(file)
        self.filedata = re.sub(r'[^a-zA-Z _-]', "", self.filedata).split()
        file.clear()
        for i in self.filedata:
            if i.lower() not in stop_words:
                file.append(i.lower())
        self.filedata = file.copy()



    def __call__(self):
        self.lemmatization()
        self.remove_stopwords()        
        return self.filename, self.filedata


if __name__ == "__main__":
    pass
