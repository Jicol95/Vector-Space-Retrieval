class document(object):

    def __init__(self, name, text):
        self.name = name
        self.text = text
        self.tokens = None

    def tokenize(self):
        tokens = self.text
        self.tokens = tokens.split()

    def term_frequency(self):
        for token in self.tokens:
            print(token)
