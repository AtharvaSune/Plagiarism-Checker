Help on function get_files in module data:

get_files(path) # function to return files with the given paths

Help on class Process in module process:

class Process(builtins.object)
| Process(filepath)
|
| Class with methods for preprocessing the text
| Methods:
| remove_stopwords: removes stopwords from the text
| lemmatize: implements lemmatization over the complete text
| get_wordnet_pos: generate POS tag for words in text
|
| Methods defined here:
|
| **call**(self)
| executes functions when object is called
| parameters:
| none
|
| returns:
| filename and processed text of the file
|
| **init**(self, filepath)
| params:
| filepath: path to file which has to be preprocessed
|
| get_wordnet_pos(self, word)
| Generated POS tag for the words in a format accepted by lemmatize() function
|
| lemmatization(self)
| Performs lemmatization on the input text
|
| remove_stopwords(self)
executes functions when object is called
parameters:
none

    returns:
        filename and processed text of the file
