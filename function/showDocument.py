# Must return a Document
# Must return a Document
def show_document():
    #my_doc is example to check code run or not
    my_doc = {
    'name': 'The Catcher in the Rye',
    'author': 'J.D. Salinger',
    'publisher': 'Little, Brown and Company',
    'yearPublish': 1951,
    'note': 'A classic coming-of-age novel'
    }

    modified_doc = modify_document(my_doc)
    print(modified_doc)

#coombine the mod function, show function and class Document to check this code is run or not
