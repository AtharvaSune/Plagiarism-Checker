import os
from data import get_docs
from calc_cosine import calc_cosine
from process_originals import process_originals

def main():
    """
        Driver method for data processing.
    """
    
    # load list of original documents
    original_docs = get_docs("original docs/*.txt") 

    # load list of test documents
    test_docs = get_docs("test docs/*.txt")

    # calculate df, tf, tf_idf for original documents
    df, tf, tf_idf = process_originals(original_docs)

    # calculate 
    for doc in test_docs:
        cos_products = calc_cosine(doc, df, tf, tf_idf)

        print(doc)
        for org_doc in cos_products:
            print(org_doc, cos_products[org_doc])

        print("\n")


if __name__ == "__main__":
    main()
