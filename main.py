from login.loginGUI import LoginGUI
import tkinter as tk
from main_classes.DocumentManage import DocumentManage

# Create a DocumentManage instance
document_manage = DocumentManage()
# Create a tk window
window = tk.Tk()
# Run the login GUI
app = LoginGUI(document_manage,window)