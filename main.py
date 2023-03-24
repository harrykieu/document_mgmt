from main_classes import DocumentBase, DocumentManage
from function import *
from login import *

# For testing purpose
# Main
docu = DocumentBase.DocumentBase("a","b","c","d","e")
docu2 = DocumentBase.DocumentBase("g","h","i","j","k")
docu3 = DocumentBase.DocumentBase("l","m","n","o","p")
docu4 = DocumentBase.DocumentBase("q","r","s","t","u")
docu5 = DocumentBase.DocumentBase("v","w","x","y","z")
dm = DocumentManage.DocumentManage()
dm._add_document(docu)
dm._add_document(docu3)
dm._add_document(docu2)
dm._add_document(docu4)
dm._add_document(docu5)
sorted_list = dm._sort_document("author")
print(sorted_list)
dm._export_csv()
