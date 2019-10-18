import math
import pickle
from process import Process

def process_originals(original_docs):
    """
        Function to calculate idf for the words found across all the originals
        an well as create vectors for original documents based on tf_idf.
        If list of originals is already processed, return from persistant storage

        Parameters:
            original_docs: input list of original documents

        Return value:
            df for all the words
            tf processed for the original documents
            tf-idf processed for the original documents
    """

    # flag to store successful file accesses
    flag = 1

    # load list of docs whose df, tf_idf has been currently stored persistantly
    try:
        with open('corpus', 'rb') as infile:
            current_list = pickle.load(infile)
    except EnvironmentError:
        flag = 0


    # if list of original docs is equal to current list, return from persistant storage
    if(flag == 1 and current_list == original_docs):
        # load df from persistant storage
        try:
            with open('df', 'rb') as infile:
                df = pickle.load(infile)
        except EnvironmentError:
            flag = 0

        # load tf from persistant storage
        try:
            with open('tf', 'rb') as infile:
                tf = pickle.load(infile)
        except EnvironmentError:
            flag = 0

        # load tf_idf from persistant storage
        try:
            with open('tf_idf', 'rb') as infile:
                tf_idf = pickle.load(infile)
        except EnvironmentError:
            flag = 0
            
        # if all file accesses have been successful return df, tf_idf
        if(flag == 1):
            return df, tf, tf_idf


    # N stores number of original documents
    N = len(original_docs)

    # df stores document frequency for all words
    df = dict()

    # tf stores term frequency for every document
    tf = dict()


    # iterate over every file and process it
    for doc in original_docs:
        proc = Process(doc)
        docname, words_list = proc()

        # append a new entry (dictionary) for current doc
        tf[doc] = dict()
        # create a temporary set to store words present in the doc
        doc_vocab = set()

        # update tf and vocabulary set for the current document
        for word in words_list:
            if (word not in doc_vocab):
                doc_vocab.add(word)
                tf[doc][word] = 1
            else:
                tf[doc][word] = tf[doc][word] + 1

        # update df according to the current document
        for word in doc_vocab:
            if(word not in df):
                df[word] = 1;
            else:
                df[word] = df[word] + 1

        del proc

    
    # tf_idf stores tf_idf for every original document
    tf_idf = tf

    # update tf_idf to store (1 + log(tf) * (1 + log(N/df)))
    for doc in tf_idf:
        for word in tf_idf[doc]:
            tf_idf[doc][word] = (1 + math.log(tf_idf[doc][word]) * (1 + math.log(N / df[word])))  


    # store list of processed docs
    with open('corpus', 'wb') as outfile:
        pickle.dump(original_docs, outfile)

    # store document frequency
    with open('df', 'wb') as outfile:
        pickle.dump(df, outfile)

    # store term frequency
    with open('tf', 'wb') as outfile:
        pickle.dump(tf, outfile)

    # store tf-idf for original docs
    with open('tf_idf', 'wb') as outfile:
        pickle.dump(tf_idf, outfile)
        

    return df, tf, tf_idf
    
    
    
    

    