import os
from data import get_docs
from calc_cosine import calc_cosine
from process_originals import process_originals

def main():
    """
        Driver method for data processing.
    """
    
    original_docs = get_docs("original docs/*.txt") 

    test_docs = get_docs("test docs/*.txt")

    df, tf, tf_idf = process_originals(original_docs)

    for doc in test_docs:
        cos_products = calc_cosine(doc, df, tf, tf_idf)

        print(doc)
        for org_doc in cos_products:
            print(cos_products[org_doc])

        print("\n")


if __name__ == "__main__":
    main()
