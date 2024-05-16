import tkinter as tk
from PIL import Image, ImageTk

from MIET.GUI.login_register_screen import create_login_register_screen


class ProfileScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Profile")
        self.root.geometry("1633x980")

        self.background_image = Image.open("poza1.png")
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        self.background_label = tk.Label(root, image=self.background_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.profile_frame = tk.Frame(root, bg="white")
        self.profile_frame.place(relx=0.5, rely=0.5, anchor="center")

        self.profile_label = tk.Label(self.profile_frame, text="Profile Information", bg="white",
                                      font=("Times New Roman", 30))
        self.profile_label.pack(pady=20)

        self.name_label = tk.Label(self.profile_frame, text="Name: John Doe", bg="white",
                                   font=("Times New Roman", 20))
        self.name_label.pack()

        self.email_label = tk.Label(self.profile_frame, text="Doctor ID: #12212", bg="white",
                                    font=("Times New Roman", 20))
        self.email_label.pack()

        self.phone_label = tk.Label(self.profile_frame, text="Hospital Department: Neurology", bg="white",
                                    font=("Times New Roman", 20))
        self.phone_label.pack()

        self.logout_button = tk.Button(self.profile_frame, text="Logout", bg="white",
                                       font=("Times New Roman", 15), command=self.logout)
        self.logout_button.pack(pady=20)

    def logout(self):
        self.root.destroy()
        create_login_register_screen()


def main():
    root = tk.Tk()
    app = ProfileScreen(root)
    root.mainloop()


if __name__ == "__main__":
    main()
