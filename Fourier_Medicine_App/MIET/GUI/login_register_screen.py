import tkinter as tk


def login():
    print("Login clicked")


def register():
    print("Register clicked")


def create_login_register_screen():
    root = tk.Tk()
    root.title("Welcome!")
    root.geometry("1600x1000")

    canvas = tk.Canvas(root, bg="lightblue")
    canvas.pack(fill="both", expand=True)

    login_frame = tk.Frame(canvas, bd=1, relief=tk.SOLID, bg="lightblue")
    login_frame.place(relx=0, rely=0, relwidth=0.5, relheight=1)

    register_frame = tk.Frame(canvas, bd=1, relief=tk.SOLID, bg="lightblue")
    register_frame.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)

    # Login Part
    login_label = tk.Label(login_frame, text="Login Form", font=("Times New Roman", 25), bg="lightblue")
    login_label.pack(pady=10)
    username_label = tk.Label(login_frame, text="Username:", font=("Times New Roman", 15), bg="lightblue")
    username_label.pack(pady=5)
    login_entry_username = tk.Entry(login_frame)
    login_entry_username.pack(pady=5)

    password_label = tk.Label(login_frame, text="Password:", font=("Times New Roman", 15), bg="lightblue")
    password_label.pack(pady=5)
    login_entry_password = tk.Entry(login_frame, show="*")
    login_entry_password.pack(pady=5)

    login_button = tk.Button(login_frame, text="Login", font=("Times New Roman", 10), command=login)
    login_button.pack(pady=10)

    # Register form
    register_label = tk.Label(register_frame, text="Register Form", font=("Times New Roman", 25), bg="lightblue")
    register_label.pack(pady=10)

    name_label = tk.Label(register_frame, text="Name:", font=("Times New Roman", 15), bg="lightblue")
    name_label.pack(pady=5)
    register_entry_name = tk.Entry(register_frame)
    register_entry_name.pack(pady=5)

    last_name_label = tk.Label(register_frame, text="Last Name:", font=("Times New Roman", 15), bg="lightblue")
    last_name_label.pack(pady=5)
    register_entry_last_name = tk.Entry(register_frame)
    register_entry_last_name.pack(pady=5)

    doctor_id_label = tk.Label(register_frame, text="Doctor ID:", font=("Times New Roman", 15), bg="lightblue")
    doctor_id_label.pack(pady=5)
    register_entry_doctor_id = tk.Entry(register_frame)
    register_entry_doctor_id.pack(pady=5)

    password_label = tk.Label(register_frame, text="Set Password:", font=("Times New Roman", 15), bg="lightblue")
    password_label.pack(pady=5)
    register_entry_password = tk.Entry(register_frame, show="*")
    register_entry_password.pack(pady=5)

    register_button = tk.Button(register_frame, text="Register", font=("Times New Roman", 10), command=register)
    register_button.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    create_login_register_screen()
