import os
import math
from document import document


class vector_space_model(object):
    """Class capable of dealing with multiple documents and can return the
    document most relevent to the search query

    __INIT__ VARS
    self.document_collection: A list of documents in the documents directory

    self.N_documents: The number of documents in the directort documents this is
    usefull for inverse documents frequency calulations.

    self.documents: A list of document objects, one to one relationship with
    document collection.

    self.inverse_document_frequency: A dictionary of words and their
    inverse_document_frequency

    self.document_return: The document object with the highest cosine similarity
    to the query document

    OBJECT FUNCTIONS

    create_documents(): Creates document objects in batch and appends them to
    documents array.

    tokenize_collection(): Tokenizes the text of each document in documents
    array.

    term_frequency_collection(): Calculates the term frequency of each token in the
    document. It makes use of a method in the document class. The point of this
    class is to call this method on all documents in one go.

    inverse_document_frequency(): Calculates the inverse_document_frequency for
    each word in all documents and puts the value in a dictionary where the key
    is the word and the value is the inverse document frequency.

    document_tf_idf(): Calculates the tf_idf of each word in each document.

    document_length(): Calculates the length of the document in it's vector
    representation.

    build_documents(): Invokes methods from this class that Calculates
    everything needed to represent documents as vectors.

    cosine_similarity(): Calculates the cosine similarity for each document with
    the query 'document'. It returns the document with the greatest cosine
    """

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
