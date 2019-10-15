import glob

# function to return files with the given paths
def get_files(path):
    return glob.glob(path)

# if __name__ == "__main__":
#     pass
help(get_files)