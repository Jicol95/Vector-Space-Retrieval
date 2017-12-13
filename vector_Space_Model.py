import os
from document import document


class vector_space_model(object):
    """Model of a document expressed as a vector"""

    def __init__(self):
        self.document_collection = os.listdir("documents/")
        self.N_documents = len(os.listdir("documents/"))
        self.documents = []
        vector_space_model.create_documents(self)
        vector_space_model.tokenize_collection(self)
        vector_space_model.term_frequency_collection(self)

    def create_documents(self):
        document_collection = self.document_collection
        documents = self.documents
        for doc in document_collection:
            f = open("documents/" + doc)
            f = f.read()
            documents.append(document(doc, f))
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
