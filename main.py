import os
import math
from data import get_files
from process import Process

if __name__ == "__main__":
    files = get_files("corpus-20090418/*.txt")
    inverted_index = {}
    files_dict = {os.path.splitext(os.path.basename(u))[0]:i+1 for i, u in enumerate(files)}
    vocabulary = set()

    for i in files:
        proc = Process(i)
        filename, filedata = proc()
        for j in filedata:            
            vocabulary.add(j)
        del proc

    print('working\n')
    vocabulary = list(vocabulary)
    vocab_dict = {}

    for word in vocabulary:
        vocab_dict[word] = len(vocab_dict)

    N = len(files_dict)
    w = len(vocab_dict)

    # print(vocab_dict)
    
    inverted_index = [set() for _ in range(len(vocab_dict))]

    # print(inverted_index)

    temp = [0] * len(vocab_dict)
    term_frequency = [temp]

    for i in range (0, len(files_dict)):
        term_frequency.append(temp)

    print('working\n')

    for doc in files:
        proc = Process(doc)
        filename, filedata = proc()

        for word in filedata:
            file_ind = files_dict[filename]
            word_ind = vocab_dict[word]            
            term_frequency[file_ind][word_ind] += 1
            inverted_index[word_ind].add(file_ind)

        del proc     
    
    print('working\n')

    doc_frequency = {}

    for word in range (0, len(inverted_index)):
        doc_frequency[word] = len(inverted_index[word])

    # print(doc_frequency)
    magn = [0] * N

    print('working\n')
    for doc in range (N):
        for word in range (w):
            term_frequency[doc][word] = (1 + math.log(term_frequency[doc][word]) * (math.log(N / doc_frequency[word] + 1))) 
            magn[doc] += (term_frequency[doc][word]) * (term_frequency[doc][word]) 
   
    # print(magn)
    
    for org in range (3):
        cosin = 0
        for i in range (w):
            cosin += term_frequency[0][i] * term_frequency[org + 26][i];
        print(cosin)
        print((cosin / (magn[0] * magn[26 + org])))
    