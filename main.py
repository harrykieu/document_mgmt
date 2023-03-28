from login.loginGUI import LoginWindow
import tkinter as tk
from login.signupGUI import SignupWindow
from login.showDocumentGUI import ShowUp, Result
from login.manageDocumentGUI import DocManage, DocWindow
from main_classes.DocumentManage import DocumentManage

# Create a DocumentManage instance
document_manage = DocumentManage()
#flow: login -> signup/signin -> show document -> manage document
loginwindow = tk.Tk()
app = LoginWindow(loginwindow,document_manage)