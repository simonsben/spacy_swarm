from poster import process_documents

documents = ['Hello there, how is it going?'] * 5


stuff = process_documents(documents)
print('Done', stuff)
