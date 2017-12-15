from vector_Space_Model import vector_space_model
from document import document
import os
import sys
import webbrowser


if __name__ == '__main__':
    # Create the vector_space_model class
    vector_space_model = vector_space_model()
    # Build the query as a document
    query_document = document("query", sys.argv[1])
    # Add that document to the list of documents
    vector_space_model.documents.append(query_document)
    vector_space_model.build_documents()
    vector_space_model.document_length()
    vector_space_model.cosine_similarity()
    try:
        webbrowser.open_new_tab("documents/" + vector_space_model.document_return.name)
    except AttributeError:
        print("No match!")
