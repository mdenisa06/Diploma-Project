import tkinter as tk

from MIET.GUI.login_register_screen import create_login_register_screen


def show_login_register_screen():

    welcome_frame.pack_forget()

    create_login_register_screen()


def create_welcome_screen():

    root = tk.Tk()
    root.title("Welcome to Your App")
    root.geometry("1500x1000")

    background_image = tk.PhotoImage(file="screen2.png")

    canvas = tk.Canvas(root, width=1500, height=1000)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor="nw", image=background_image)

    global welcome_frame
    welcome_frame = tk.Frame(canvas, bg="#FDFDFD")
    welcome_frame.place(relx=0.5, rely=0.5, anchor="center")

    logo_image = tk.PhotoImage(file="doctor.png")  # Replace with your image file
    logo_label = tk.Label(welcome_frame, image=logo_image, bg="#FDFDFD", fg="black")
    logo_label.image = logo_image  # Retain a reference to the image object
    logo_label.pack(pady=20)

    app_name_label = tk.Label(welcome_frame, text="ImaGenius", font=("Times New Roman", 50), bg="#FDFDFD", fg="black")
    app_name_label.pack(pady=10)

    root.after(5000, show_login_register_screen)

    root.mainloop()


if __name__ == "__main__":
    create_welcome_screen()
