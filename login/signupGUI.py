import tkinter as tk

class Signup:
    def __init__(self, username_input, password_input):
        self.username_input = username_input
        self.password_input = password_input

    def create_account(self):
        username = self.username_input.get()
        password = self.password_input.get()

        with open("nonadmin.dat") as f:
            data = f.read().strip()
            if "\nEnd\n" not in data:
                print("Invalid file format")
                return
            usernames, passwords = data.split("\nEnd\n")
            usernames = usernames.strip().split("\n")
            passwords = passwords.strip().split("\n")

        if username in usernames:
            print("Username is already taken.")
            return

        usernames.append(username)
        passwords.append(password)

        with open("nonadmin.dat", "w") as f:
            f.write("\n".join(usernames) + "\nEnd\n" + "\n".join(passwords))

        print("Account created successfully.")

class SignupWindow:
    def __init__(self, master):
        self.master = master
        master.title("Signup Window")

        signup_frame = tk.Frame(master)
        signup_frame.pack(padx=10, pady=10)

        username_label = tk.Label(signup_frame, text="Username:")
        username_label.pack(padx=10, pady=10)
        self.username_input = tk.Entry(signup_frame)
        self.username_input.pack(padx=10, pady=10)

        password_label = tk.Label(signup_frame, text="Password:")
        password_label.pack(padx=10, pady=10)
        self.password_input = tk.Entry(signup_frame, show="*")
        self.password_input.pack(padx=10, pady=10)

        signup = Signup(self.username_input, self.password_input)
        signup_button = tk.Button(signup_frame, text="Sign up", command=signup.create_account)
        signup_button.pack(padx=10, pady=10)


