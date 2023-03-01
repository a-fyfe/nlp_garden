# Compulsory Task - Garden Path Sentences

# Importing spaCy

import spacy

nlp = spacy.load('en_core_web_sm')

# Creating list of garden path sentences

gardenpathSentences = ["We painted the Ford with cracks.",
                    "The raft floated down the British river sank.",
                    "The man who whistles writes the Patriot Act.",
                    "David gave the child the dog bit a plaster.",
                    "When John eats food gets thrown.",
                    ]

# Tokenising each garden path sentence in the list

for item in gardenpathSentences:
    print("Garden path sentence: " + item)
    
    token = nlp(item)
    token.text.split()
    tokenised = [token.orth_ for token in token]
    print("Tokenised sentence: {}".format(tokenised))

    # Entity recognition for the garden path sentences
    print([(i, i.label_, i.label) for i in nlp(item).ents])

# Looking up entities

print("\nLooking up entities:\n")
print(spacy.explain("ORG"))

print(spacy.explain("LAW"))

print(spacy.explain("PERSON"))

print(spacy.explain("NORP"))

# Additional detail on entities

# LAW

"""
The LAW entity signifies that a common legal documents (most commonly a named piece of US legislation)
has been recognised. In this case the well-known piece of US legislation, the Patriot Act, was correctly
recognised.
"""

# NORP

"""
The NORP entity (standing for Nationalities, religious, political groups) signifies that a nationality or
regional label has been recognisd. In this case the national identifier, British, was correctly recognised.
"""
