from doetc import DocManage, DocWindow

class Login:
    def __init__(self, username_input, password_input):
        self.username_input = username_input
        self.password_input = password_input

    def check_user_pass(file_path, username, password):
        with open(file_path) as f:
            data = f.read().strip()
            if "\nEnd\n" not in data:
                print("Invalid file format")
                return False
            usernames, passwords = data.split("\nEnd\n")
            usernames = usernames.strip().split("\n")
            passwords = passwords.strip().split("\n")

        for i in range(len(usernames)):
            if usernames[i] == username and passwords[i] == password:
                return True
        return False

    def signin(self):
        username = self.username_input.get()
        password = self.password_input.get()

        if Login.check_user_pass("admin.dat", username, password):
            print("Admin Login Successful!")
            window = DocWindow(admin=True)
            window.show_options()
        elif Login.check_user_pass("nonadmin.dat", username, password):
            print("Non-admin Login Successful!")
            window = DocWindow(admin=False)
            window.show_options()
        else:
            print("Invalid username or password.")


    

