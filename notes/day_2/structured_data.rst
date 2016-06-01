Converting Unstructured Text to Structured Text
===============================================

Steps
-----

Scrape to data to something clean (eg to CSV)
*********************************************

``csv.DictReader``

Tokenize: what is the smallest / biggest information you need. (eg, bigram, word)
*********************************************************************************

``NLTK`` (Natural language toolkit) is your friend for this.

You can also use Parsey McParseface

Bag of Words
************

Remove the most common words. Throw out the ones that only appear once
