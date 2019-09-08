import os
from data import get_files
from process import Process

if __name__ == "__main__":
    files = get_files("corpus-20090418/*.txt")
    inverted_index = {}
    files_dict = {os.path.splitext(os.path.basename(u))[0]:i+1 for i, u in enumerate(files)}
    for i in files:
        proc = Process(i)
        filename, filedata = proc()
        for j in filedata:
            if j in inverted_index.keys():
                inverted_index[j].append(files_dict[filename])
            else:
                inverted_index[j] = [files_dict[filename]]

        del proc


    for i in inverted_index:
        inverted_index[i] = sorted(list(set(inverted_index[i])))
        inverted_index[i].append('\\' + str(len(inverted_index[i])) + '\\')
    
    print(inverted_index['inheritance'])