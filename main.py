from data import get_files
from process import Process

if __name__ == "__main__":
    files = get_files("corpus-20090418/*.txt")
    inverted_index = {}
    for i in files:
        print(i)
        proc = Process(i)
        filename, filedata = proc()
        
        for j in filedata:
            if j in inverted_index.keys():
                inverted_index[j].append(filename)
            else:
                inverted_index[j] = [filename]

        del proc

    print(inverted_index)        