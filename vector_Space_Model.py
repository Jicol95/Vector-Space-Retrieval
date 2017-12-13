import os
import math
from document import document


class vector_space_model(object):
    """Model of a document expressed as a vector"""

    def __init__(self):
        self.document_collection = os.listdir("documents/")
        self.N_documents = len(os.listdir("documents/"))
        self.documents = []
        self.inverse_document_frequency = {}
        vector_space_model.create_documents(self)
        vector_space_model.tokenize_collection(self)
        vector_space_model.term_frequency_collection(self)
        vector_space_model.inverse_document_frequency(self)

    def create_documents(self):
        document_collection = self.document_collection
        documents = self.documents
        for doc in document_collection:
            f = open("documents/" + doc)
            text = f.read()
            f.close()
            documents.append(document(doc, text))
            self.documents = documents

    def tokenize_collection(self):
        documents = self.documents
        for doc in documents:
            doc.tokenize()

    def term_frequency_collection(self):
        documents = self.documents
        for doc in documents:
            doc.calculate_term_frequency()

    def inverse_document_frequency(self):
        N_documents = self.N_documents
        documents = self.documents
        inverse_document_frequency = self.inverse_document_frequency
        word_count = 0
        for doc in documents:
            for word in doc.tokens:
                for d in documents:
                    if word in d.tokens:
                        word_count += 1
                x = float(math.log2(float(N_documents) / float(word_count)))
                print(x)
                self.inverse_document_frequency[word] = x
                word_count = 0
