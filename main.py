import os
import math
import pickle
from data import get_docs
from process import Process
from calc_cosine import calc_cosine
from process_originals import process_originals

# for

def main():
    """
        Driver method for data processing.
    """
    
    original_docs = get_docs("original docs/*.txt") 

    test_docs = get_docs("test docs/*.txt")

    df, tf_idf = process_originals(original_docs) 


if __name__ == "__main__":
    main()
