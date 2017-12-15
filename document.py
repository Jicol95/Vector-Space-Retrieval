import re


class document(object):
    """
    Class that represents a document which is compatibile with vector space
    model.

    __INIT__ VARS

    self.name: File name of the document
    self.text: The contents of the File
    self.term_frequency: The term frequency of each word in the document
    self.tf_idf: The term_frequency * inverse_document_frequency of each word
    self.tokens: The tokenized form of self.text
    self.length: The length of the document as a vector_space_model

    OBJECT METHODS

    tokenize(): Tokenizes self.text and passes the vaule to self.tokens

    calculate_term_frequency(): Counts the frequency of each unique word in the
    document.
    """

    def __init__(self, name, text):
        self.name = name
        self.text = re.sub(r'[^\w\s]', '', text)
        self.term_frequency = {}
        self.tf_idf = {}
        self.tokens = None
        self.length = None

    def tokenize(self):
        tokens = self.text
        self.tokens = tokens.split()

    def calculate_term_frequency(self):
        tokens = self.tokens
        term_frequency = self.term_frequency

        for token in tokens:
            if not(token in term_frequency):
                term_frequency[token] = 1
            elif token in term_frequency:
                term_frequency[token] = term_frequency[token] + 1

        self.term_frequency = term_frequency
