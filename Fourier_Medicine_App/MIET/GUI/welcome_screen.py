import tkinter as tk


def show_login_register_screen(callback):
    callback()


def create_welcome_screen(root, callback):
    global background_image, logo_image

    root.title("Welcome to ImaGenius")
    root.geometry("1633x980")

    background_image = tk.PhotoImage(file="poza1.png")

    canvas = tk.Canvas(root, width=1633, height=900)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor="nw", image=background_image)

    welcome_frame = tk.Frame(canvas, bg="white")
    welcome_frame.place(relx=0.5, rely=0.5, anchor="center")

    logo_image = tk.PhotoImage(file="doctor.png")
    logo_label = tk.Label(welcome_frame, image=logo_image, bg="white")
    logo_label.pack(pady=10)

    app_name_label = tk.Label(welcome_frame, text="ImaGenius", font=("Times New Roman", 75, "bold"), bg="white")
    app_name_label.pack(pady=10)

    root.after(5000, lambda: show_login_register_screen(callback))


if __name__ == "__main__":
    root = tk.Tk()
    create_welcome_screen(root, lambda: print("Callback after welcome screen"))
    root.mainloop()
