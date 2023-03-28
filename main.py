from login.loginGUI import LoginWindow
import tkinter as tk
from main_classes.DocumentManage import DocumentManage

# Create a DocumentManage instance
document_manage = DocumentManage()
#flow: login -> signup/signin -> show document -> manage document
loginwindow = tk.Tk()
# insert image as background

app = LoginWindow(loginwindow,document_manage)