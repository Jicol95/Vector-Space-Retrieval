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
        self.document_return = None

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
                x = float(math.log(float(N_documents) / float(word_count), 2))
                self.inverse_document_frequency[word] = x
                word_count = 0

    def document_tf_idf(self):
        documents = self.documents
        inverse_document_frequency = self.inverse_document_frequency
        for doc in documents:
            for word in doc.tokens:
                doc.tf_idf[word] = doc.term_frequency[word] * inverse_document_frequency[word]

    def document_length(self):
        documents = self.documents
        for doc in documents:
            tokens = doc.tokens
            values = []
            for token in tokens:
                values.append(doc.tf_idf[token])
            for value in values:
                value ** 2
            doc.length = math.sqrt(sum(values))

    def build_documents(self):
        vector_space_model.create_documents(self)
        vector_space_model.tokenize_collection(self)
        vector_space_model.term_frequency_collection(self)
        vector_space_model.inverse_document_frequency(self)
        vector_space_model.document_tf_idf(self)

    def cosine_similarity(self):
        documents = self.documents
        query = documents[0]
        document_best_similarity = 0
        for doc in documents[1:]:
            vaules = []
            for token in doc.tokens:
                doc_tf_idf = doc.tf_idf.get(token, 0)
                query_tf_idf = query.tf_idf.get(token, 0)
                vaules.append(doc_tf_idf * query_tf_idf)
            numerator = sum(vaules)
            denomenator = query.length + doc.length
            similarity = numerator / denomenator
            if similarity > document_best_similarity:
                document_best_similarity = similarity
                self.document_return = doc
        self.documents = documents[1:]
