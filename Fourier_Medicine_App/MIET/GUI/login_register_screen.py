import tkinter as tk
from tkinter import PhotoImage, Entry, messagebox
from register import register_account
from login import login_account


def create_login_register_screen(root, on_login_success):
    def register():
        name = register_entry_name.get()
        last_name = register_entry_last_name.get()
        doctor_id = register_entry_doctor_id.get()
        password = register_entry_password.get()

        if not name or not last_name or not doctor_id or not password:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        if register_account(name, last_name, doctor_id, password):
            register_entry_name.delete(0, tk.END)
            register_entry_last_name.delete(0, tk.END)
            register_entry_doctor_id.delete(0, tk.END)
            register_entry_password.delete(0, tk.END)
            messagebox.showinfo("Success", "Account created.")
        else:
            messagebox.showerror("Error", "Email already exists.")

    def login():
        email = login_entry_username.get()
        password = login_entry_password.get()
        result = login_account(email, password)
        if isinstance(result, tuple) and len(result) >= 2:
            message, uid = result
            if message == "Login successful":
                messagebox.showinfo("Success", message)
                on_login_success(uid)
            else:
                messagebox.showerror("Error", message)
        else:
            messagebox.showerror("Error", "Unexpected error occurred during login.")

    root.title("Login or Create Account")
    root.geometry("1633x980")
    image_path = PhotoImage(file="poza1.png")
    root.image_path = image_path
    bg_image = tk.Label(root, image=image_path)
    bg_image.place(x=0, y=0, relwidth=1, relheight=1)

    login_label = tk.Label(root, text="Login Form", font=("Times New Roman", 35, "bold"), bg="white")
    login_label.place(relx=0.25, rely=0.3, anchor="center")

    global login_entry_username, login_entry_password

    username_label = tk.Label(root, text="Username:", font=("Times New Roman", 15, "bold"), bg="white")
    username_label.place(relx=0.15, rely=0.45, anchor="center")
    login_entry_username = Entry(root)
    login_entry_username.place(relx=0.25, rely=0.45, anchor="center")

    password_label = tk.Label(root, text="Password:", font=("Times New Roman", 15, "bold"), bg="white")
    password_label.place(relx=0.15, rely=0.5, anchor="center")
    login_entry_password = Entry(root, show="*")
    login_entry_password.place(relx=0.25, rely=0.5, anchor="center")

    login_button = tk.Button(root, text="Login", font=("Times New Roman", 10, "bold"), command=login)
    login_button.place(relx=0.25, rely=0.55, anchor="center")

    register_label = tk.Label(root, text="Register Form", font=("Times New Roman", 35, "bold"), bg="white")
    register_label.place(relx=0.75, rely=0.3, anchor="center")

    global register_entry_name, register_entry_last_name, register_entry_doctor_id, register_entry_password

    name_label = tk.Label(root, text="Name:", font=("Times New Roman", 15, "bold"), bg="white")
    name_label.place(relx=0.65, rely=0.45, anchor="center")
    register_entry_name = Entry(root)
    register_entry_name.place(relx=0.75, rely=0.45, anchor="center")

    last_name_label = tk.Label(root, text="Last Name:", font=("Times New Roman", 15, "bold"), bg="white")
    last_name_label.place(relx=0.65, rely=0.5, anchor="center")
    register_entry_last_name = Entry(root)
    register_entry_last_name.place(relx=0.75, rely=0.5, anchor="center")

    doctor_id_label = tk.Label(root, text="Doctor ID:", font=("Times New Roman", 15, "bold"), bg="white")
    doctor_id_label.place(relx=0.65, rely=0.55, anchor="center")
    register_entry_doctor_id = Entry(root)
    register_entry_doctor_id.place(relx=0.75, rely=0.55, anchor="center")

    password_label = tk.Label(root, text="Password:", font=("Times New Roman", 15, "bold"), bg="white")
    password_label.place(relx=0.65, rely=0.6, anchor="center")
    register_entry_password = Entry(root, show="*")
    register_entry_password.place(relx=0.75, rely=0.6, anchor="center")

    register_button = tk.Button(root, text="Register", font=("Times New Roman", 10, "bold"), command=register)
    register_button.place(relx=0.75, rely=0.65, anchor="center")


if __name__ == "__main__":
    root = tk.Tk()
    create_login_register_screen(root, lambda user_info: print(f"Logged in user info: {user_info}"))
    root.mainloop()
