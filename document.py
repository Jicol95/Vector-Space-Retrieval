import math


class document(object):

    def __init__(self, name, text):
        self.name = name
        self.text = text
        self.term_frequency = {}
        self.inverse_document_frequency = {}
        self.tokens = None

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
