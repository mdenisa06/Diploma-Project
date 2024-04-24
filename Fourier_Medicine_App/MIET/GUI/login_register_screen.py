import tkinter as tk
from tkinter import PhotoImage


def login():
    print("Login clicked")


def register():
    print("Register clicked")


def create_login_register_screen():
    root = tk.Tk()
    root.title("Welcome!")
    root.geometry("1500x1000")

    image_path = PhotoImage(
        file=r"C:\Users\Denisa\Desktop\Diploma Project\Diploma-Project\Fourier_Medicine_App\MIET\GUI\screen2.png")
    bg_image = tk.Label(root, image=image_path)
    bg_image.place(x=0, y=0, relwidth=1, relheight=1)

    # Login Part
    login_label = tk.Label(root, text="Login Form", font=("Times New Roman", 25), bg="#FDFDFD", fg="black")
    login_label.place(relx=0.25, rely=0.3, anchor="center")

    username_label = tk.Label(root, text="Username:", font=("Times New Roman", 15), bg=root['bg'], fg="black")
    username_label.place(relx=0.15, rely=0.45, anchor="center")
    login_entry_username = tk.Entry(root)
    login_entry_username.place(relx=0.25, rely=0.45, anchor="center")

    password_label = tk.Label(root, text="Password:", font=("Times New Roman", 15), bg=root['bg'], fg="black")
    password_label.place(relx=0.15, rely=0.5, anchor="center")
    login_entry_password = tk.Entry(root, show="*")
    login_entry_password.place(relx=0.25, rely=0.5, anchor="center")

    login_button = tk.Button(root, text="Login", font=("Times New Roman", 10), command=login)
    login_button.place(relx=0.25, rely=0.55, anchor="center")

    # Register Part
    register_label = tk.Label(root, text="Register Form", font=("Times New Roman", 25), bg="#FDFDFD", fg="black")
    register_label.place(relx=0.75, rely=0.3, anchor="center")

    name_label = tk.Label(root, text="Name:", font=("Times New Roman", 15), bg=root['bg'], fg="black")
    name_label.place(relx=0.65, rely=0.45, anchor="center")
    register_entry_name = tk.Entry(root)
    register_entry_name.place(relx=0.75, rely=0.45, anchor="center")

    last_name_label = tk.Label(root, text="Last Name:", font=("Times New Roman", 15), bg=root['bg'], fg="black")
    last_name_label.place(relx=0.65, rely=0.5, anchor="center")
    register_entry_last_name = tk.Entry(root)
    register_entry_last_name.place(relx=0.75, rely=0.5, anchor="center")

    doctor_id_label = tk.Label(root, text="Doctor ID:", font=("Times New Roman", 15), bg=root['bg'], fg="black")
    doctor_id_label.place(relx=0.65, rely=0.55, anchor="center")
    register_entry_doctor_id = tk.Entry(root)
    register_entry_doctor_id.place(relx=0.75, rely=0.55, anchor="center")

    password_label = tk.Label(root, text="Set Password:", font=("Times New Roman", 15), bg=root['bg'], fg="black")
    password_label.place(relx=0.65, rely=0.6, anchor="center")
    register_entry_password = tk.Entry(root, show="*")
    register_entry_password.place(relx=0.75, rely=0.6, anchor="center")

    register_button = tk.Button(root, text="Register", font=("Times New Roman", 10), command=register)
    register_button.place(relx=0.75, rely=0.65, anchor="center")

    root.mainloop()


if __name__ == "__main__":
    create_login_register_screen()
