import math
from process import Process

def calc_cosine(doc, df, org_tf, org_tf_idf):

    """
        Calculates normalized cosine product of document with every test document

        Parameters:
            doc: test document
            df: document frequency for the corpus
            org_tf: term frequncy table for original documents
            org_tf_idf: tf_idf table for original documents

        Return Value:
            Normalized cosine product of document with every test document
    """

    # Store number of original documents
    N = len(df)

    # Preprocess document to remove stop words etc.
    proc = Process(doc)
    filename, words_list = proc()

    # tf stores term frequency for each term in the document
    tf = dict()


    # calculate term frequency for each term in the document
    for word in words_list:
        if(word not in tf):
            tf[word] = 1
        else:
            tf[word] = tf[word] + 1


    # tf_idf stores tf_idf for the document
    tf_idf = tf


    # calculate tf_idf for the document
    for word in tf_idf:
        if(word in df):
            tf_idf[word] = (1 + math.log(tf_idf[word]) * (1 + math.log(N / df[word])))


    # to store normalized cosine product of document with every test document
    cos_products = dict()
    

    # iterate over every original document
    for org_doc in org_tf:
        cos_products[org_doc] = 0
        # to store magnitude of document
        magn_doc = 0
        # to store magnitude of original document
        magn_org = 0

        # calculate magnitude of document and find cosine product
        for word in tf:
            magn_doc += tf[word] * tf[word]
            if word in org_tf[org_doc]:
                cos_products[org_doc] += tf_idf[word] * org_tf_idf[org_doc][word]

        # calculate magnitude of original document
        for word in org_tf[org_doc]:
            magn_org += org_tf[org_doc][word] * org_tf[org_doc][word]

        # normalize the cosine product
        cos_products[org_doc] /= (magn_doc * magn_org) 

    
    # return normalized cosine products
    return cos_products
