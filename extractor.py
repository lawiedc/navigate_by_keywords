#!/usr/bin/python3

## extractor.py ##

# Extract the keywords from a set of pdfs and show most common keywords across all pdfs
# Show how much pdfs have in common with these words by showing how many keywords they contain

from sklearn.feature_extraction.text import CountVectorizer

import os
import fitz # To handle pdfs
import pprint

max_terms = 10
srcdir = os.getcwd() + "/pdfs"
pdf_set = set()
full_summ = {}
used_words = {}
most_used_words = {}
doc_centrality = {}

# Extract text from a set of pdfs
## For this sketch, the set of pdfs has been downloaded in advance
## In a mature solution, this would crawl the site for content of all types

for pdf in os.listdir(srcdir):
    pdf_set.add(pdf) 

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
            used_words[word].add(pdf)
        else:
            used_words[word] = {pdf}

# Get used_words which appeared in more than one doc
for word in used_words:
    if len(used_words[word]) > 1:
        most_used_words[word] = used_words[word]

# Sort by most seen and print

print("\nFor overall commonality, list the words which were in the top set for more than one doc, and the docs\n")
print("word: number of docs: total appearances where key: list of docs where this is a key word ")

for word in sorted(most_used_words.keys()):
    print(word, len(most_used_words[word]), full_summ[word], sep=': ', end=':\t')
    print(*sorted(most_used_words[word]), sep=', ')
    
    for doc in most_used_words[word]:
        if doc in doc_centrality:
            doc_centrality[doc] = doc_centrality[doc] + 1
        else:
            doc_centrality[doc] = 1

print("\nAlso print the list of docs with how many key words they have")
print("More is an indication they are more central to this list")

# TODO - make this code more succinct
last_count = -1
for key, value in sorted(doc_centrality.items(), key=lambda item: item[1], reverse=True):
    if value != last_count:
        print( "\n", value)
        last_count = value
    else:
        print( ', ', end='')

    print( key, end='' )
    pdf_set.remove(key)

if len(pdf_set) > 0:
    print( "\n 0")
    print( *sorted(pdf_set), sep=', ')  

