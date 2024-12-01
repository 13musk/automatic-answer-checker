import tkinter as tk
from tkinter import messagebox
from answer_checker import AnswerChecker

users = {"admin": "password"}  

class LoginSignupApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Automatic Answer Checker")
        self.root.geometry("350x550")
        self.root.resizable(False, False)
        self.login_page()

    def login_page(self):
        
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Automatic Answer\n Checker", font=("Rockwell", 30, "bold"), fg="#03A9F4").pack(pady=20)

        tk.Label(self.root, text="Login", font=("Arial", 30, "bold")).pack(pady=20)

        tk.Label(self.root, text="Username:", font=("Arial", 20)).pack(anchor="w", padx=50)
        self.username_entry = tk.Entry(self.root, font=("Arial", 15))
        self.username_entry.pack(pady=5, padx=50)

        tk.Label(self.root, text="Password:", font=("Arial", 20)).pack(anchor="w", padx=50)
        self.password_entry = tk.Entry(self.root, font=("Arial", 15), show="*")
        self.password_entry.pack(pady=5, padx=50)

        tk.Button(self.root, text="Login", font=("Arial", 15), command=self.login).pack(pady=10)

        tk.Label(self.root, text="Don't have an account?", font=("Arial", 15)).pack(pady=5)
        tk.Button(self.root, text="Sign Up", font=("Arial", 10), command=self.signup_page).pack()

    def signup_page(self):
        
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Sign Up", font=("Arial", 30, "bold")).pack(pady=20)

        tk.Label(self.root, text="Username:", font=("Arial", 20)).pack(anchor="w", padx=50)
        self.new_username_entry = tk.Entry(self.root, font=("Arial", 15))
        self.new_username_entry.pack(pady=5, padx=50)

        tk.Label(self.root, text="Password:", font=("Arial", 20)).pack(anchor="w", padx=50)
        self.new_password_entry = tk.Entry(self.root, font=("Arial", 15), show="*")
        self.new_password_entry.pack(pady=5, padx=50)

        tk.Button(self.root, text="Sign Up", font=("Arial", 15), command=self.signup).pack(pady=10)

        tk.Button(self.root, text="Back to Login", font=("Arial", 10), command=self.login_page).pack(pady=5)

    def login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if username in users and users[username] == password:
            messagebox.showinfo("Login Success", "Welcome!")
            self.open_answer_checker()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    def signup(self):
        username = self.new_username_entry.get().strip()
        password = self.new_password_entry.get().strip()

        if not username or not password:
            messagebox.showwarning("Input Error", "All fields are required!")
            return

        if username in users:
            messagebox.showerror("Signup Error", "Username already exists!")
            return

        users[username] = password
        messagebox.showinfo("Signup Success", "Account created successfully!")
        self.login_page()

    def open_answer_checker(self):
       
        for widget in self.root.winfo_children():
            widget.destroy()
        AnswerChecker(self.root)
        
if __name__ == "__main__":
    root = tk.Tk()
    LoginSignupApp(root)
    root.mainloop()
