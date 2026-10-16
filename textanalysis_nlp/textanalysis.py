import nltk



# Downloading NLTK data for NER

nltk.download('maxent_ne_chunker')
nltk.download('maxent_ne_chunker_tab')
nltk.download('words')

nltk.download('punkt')
nltk.download('punkt_tab')

nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')





# Sample business document

business_document = """

The recent feedback from Acme Corp highlighted issues with the new model of the Omega widget.

Customers from New York and San Francisco have reported delays in shipping.

The CEO of Acme Corp, Jane Doe, mentioned plans to address these concerns by Q3.

"""



# Tokenizing the document

tokens = nltk.word_tokenize(business_document)

# Applying NER

ner_result = nltk.ne_chunk(nltk.pos_tag(tokens))

# Printing named entities
print("Named Entities:")
for entity in ner_result:
    if isinstance(entity, nltk.Tree):
        print(" ".join([word for word, tag in entity.leaves()]))

# Printing named entities along with their categories
print("\nNamed Entities with Categories:")
for entity in ner_result:
    if isinstance(entity, nltk.Tree):
        entity_name = " ".join([word for word, tag in entity.leaves()])
        entity_category = entity.label()
        print(f"{entity_name}: {entity_category}")

# Sample business document
business_document = """
The recent feedback from Acme Corp highlighted issues with the new model of the Omega widget.
Customers from New York and San Francisco have reported delays in shipping.
The CEO of Acme Corp, Jane Doe, mentioned plans to address these concerns by Q3.
"""

# Tokenizing the document
tokens = nltk.word_tokenize(business_document)

# Applying POS tagging
pos_tags = nltk.pos_tag(tokens)

# Printing words and their POS tags
print("Words and POS Tags:")
for word, tag in pos_tags:
    print(f"{word}: {tag}")

