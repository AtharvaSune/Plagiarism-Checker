import math
from process import Process

def calc_cosine(files, file_index, vocabulary):

    """
        Calculates cosine product using tf-idf
        Returns a dictionary, having key: document nameINCOMPLETE value pair of cosine products for the input list of test documents
    """
    
    inverted_index = {}
    vocabulary = list(vocabulary)
    word_index = {}

    for word in vocabulary:
        word_index[word] = len(word_index)

    N = len(file_index)
    w = len(word_index)

    print(N, ' ', w)
    # print(word_index)
    
    inverted_index = [set() for _ in range(len(word_index))]

    # print(inverted_index)

    temp = [0] * len(word_index)
    term_frequency = [temp]

    for i in range (0, len(file_index)):
        term_frequency.append(temp)

    print('working\n')

    for doc in files:
        proc = Process(doc)
        filename, words_list = proc()

        for word in words_list:
            file_ind = file_index[filename]
            word_ind = word_index[word]            
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
    cosines_list = dict()
    for org in range (3):
        cosin = 0
        for i in range (w):
            cosin += term_frequency[0][i] * term_frequency[org + 26][i];
        print(cosin)
        print((cosin / (magn[0] * magn[26 + org])))
    
    return cosines_list


# if __name__ == "__main__":
#     main()
    
#     help(main)
    
#     # print(inverted_index['inheritance'])
