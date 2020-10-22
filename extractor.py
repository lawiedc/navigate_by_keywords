#!/usr/bin/python3

## extractor.py ##

# Extract the keywords from a set of pdfs and show most common keywords across all pdfs
# This can be extended to build a graph of the pdfs by relatedness of keywords

from sklearn.feature_extraction.text import CountVectorizer

import os
import fitz # To handle pdfs
import pprint

max_terms = 10
srcdir = os.getcwd() + "/pdfs"
full_summ = {}
used_words = {}
most_used_words = {}

# Extract text from a set of pdfs
## For this sketch, the set of pdfs has been downloaded in advance
## In a mature solution, this would crawl the site for content of all types

for pdf in os.listdir(srcdir):
    print(pdf)

    text = ""

    with fitz.open( srcdir + "/" + pdf) as srcdoc:
        for page in srcdoc:
            text += page.getText()         

    # Obtain keywords from extracted text
    ## CountVectorizer doesn't natively handle stemming
    ## e.g. city / cities

    cv = CountVectorizer(stop_words="english", max_features=max_terms)
    counts = cv.fit_transform([text]).toarray().ravel()
    words = cv.get_feature_names()

    pdf_summ = dict(zip(words, counts))

    # pprint.pprint(pdf_summ)

    # Store top keywords across all docs
    # In full_summ, longer docs will develop an advantage
    full_summ = { **full_summ, **pdf_summ}

    # In used_words, only counting words once per doc
    # to get an idea of keywords across docs
    for word in words:
        if word in used_words:
            used_words[word] = used_words[word] + 1
        else:
            used_words[word] = 1

# Get used_words which appeared more than once
for word in used_words:
    if used_words[word] > 1:
        most_used_words[word] = used_words[word]


# Sort by most seen and print
print("First list all the words that were in the top set for at least one doc.")
print("Ordered by how often they appeared in all docs")
print({key: value for key, value in sorted(full_summ.items(), key=lambda item: item[1], reverse=True)})

print("To compare for overall commonality,")
print("Also list the words which were in the top set for more than one doc")
print({key: value for key, value in sorted(most_used_words.items(), key=lambda item: item[1], reverse=True)})




  

