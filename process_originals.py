import math
import pickle
from process import Process

def process_originals(original_files):
    """
        Function to calculate idf for the words found across all the originals
        an well as create vectors for original documents based on tf_idf.
        If list of originals is already processed, return from persistant storage

        Parameters:
            original_files: input list of original documents

        Return value:
            idf for all the words
            tf-idf processed for the original documents
    """

    # flag to store successful file accesses
    flag = 1

    # load list of files whose df, tf_idf has been currently stored persistantly
    try:
        with open('corpus', 'rb') as infile:
            current_list = pickle.load(infile)
    except EnvironmentError:
        flag = 0


    # if list of original files is equal to current list, return from persistant storage
    if(flag == 1 and current_list == original_files):
        # load df from persistant storage
        try:
            with open('df', 'rb') as infile:
                df = pickle.load(infile)
        except EnvironmentError:
            flag = 0

        # load df from persistant storage
        try:
            with open('tf_idf', 'rb') as infile:
                tf_idf = pickle.load(infile)
        except EnvironmentError:
            flag = 0
            
        # if all file accesses have been successful return df, tf_idf
        if(flag == 1)
            return df, tf_idf

    # N stores number of original documents
    N = len(original_files)

    # df stores document frequency for all words
    df = dict()

    # tf_idf stores tf for every original file
    tf_idf = dict()

    # iterate over every file and process it
    for file in original_files:
        proc = Process(file)
        filename, words_list = proc()

        # append a new entry (dictionary) for current file
        tf_idf[file] = dict()
        # create a temporary set to store words present in the file
        file_vocab = set()

        # update tf and vocabulary set for the current document
        for word in words_list:
            if (word not in file_vocab):
                file_vocab.add(word)
                tf_idf[file][word] = 1
            else:
                tf_idf[file][word] = tf_idf[file][word] + 1


        # update df according to the current document
        for word in file_vocab:
            if(word not in df):
                df[word] = 1;
            else:
                df[word] = df[word] + 1

        del proc


    # update tf_idf to store (1 + log(tf) * (1 + log(N/df)))
    for file in tf_idf:
        for word in tf_idf[file]:
            tf_idf[file][word] = (1 + math.log(tf_idf[file][word]) * (1 + math.log(N / df[word])))

    

    # store list of processed files
    filename = 'corpus'
    outfile = open(filename, 'wb')
    pickle.dump(original_files, outfile)
    outfile.close()

    # store document frequency
    filename = 'df'
    outfile = open(filename, 'wb')
    pickle.dump(df, outfile)
    outfile.close()

    # store tf-idf for original files
    filename = 'tf_idf'
    outfile = open(filename, 'wb')
    pickle.dump(tf_idf, outfile)
    outfile.close()

    # return updated vocabulary
    return df, tf_idf
    
    
    
    

    