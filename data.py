import glob

# function to return files with the given paths
def get_docs(path):
    return glob.glob(path)
