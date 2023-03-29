from login.loginGUI import LoginGUI
import tkinter as tk
from main_classes.DocumentManage import DocumentManage

# Create a DocumentManage instance
document_manage = DocumentManage()
#flow: login -> signup/signin -> show document -> manage document
window = tk.Tk()
# insert image as background

app = LoginGUI(document_manage,window)