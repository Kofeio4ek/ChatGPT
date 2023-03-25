import tkinter as tk

def login():
    username = username_input.get()
    password = password_input.get()
    
    # Perform login authentication here
    
    if username == "admin" and password == "password":
        print("Login successful")
    else:
        print("Invalid username or password")

root = tk.Tk()
root.geometry("300x200")
root.title("Login Form")

username_label = tk.Label(root, text="Username:")
username_label.place(x=50, y=50)

username_input = tk.Entry(root)
username_input.place(x=120, y=50)

password_label = tk.Label(root, text="Password:")
password_label.place(x=50, y=80)

password_input = tk.Entry(root, show="*")
password_input.place(x=120, y=80)

login_button = tk.Button(root, text="Login", command=login)
login_button.place(x=120, y=120)

root.mainloop()
