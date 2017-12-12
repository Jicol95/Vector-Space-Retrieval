from document import document
import os

documents = os.listdir("documents/")


d1 = document("test1", "new york times")
d1.tokenize()
d1.term_frequency()
