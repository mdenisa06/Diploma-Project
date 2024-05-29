import tkinter as tk
from PIL import Image, ImageTk
import os
import sys
from firebase_init import db


class ProfileScreen:
    def __init__(self, root, current_user_info, on_logout):
        self.root = root
        self.root.title("Profile")
        self.root.geometry("1633x980")

        self.current_user_info = current_user_info
        self.on_logout = on_logout

        if hasattr(sys, '_MEIPASS'):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.abspath(".")

        background_image_path = os.path.join(base_path, "poza1.png")
        self.background_image = Image.open(background_image_path)
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        self.background_label = tk.Label(root, image=self.background_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.profile_frame = tk.Frame(root, bg="white")
        self.profile_frame.place(relx=0.5, rely=0.5, anchor="center")

        self.profile_label = tk.Label(self.profile_frame, text="Profile Information", bg="white",
                                      font=("Times New Roman", 30))
        self.profile_label.pack(pady=20)

        self.display_user_info()

        self.logout_button = tk.Button(self.profile_frame, text="Logout", bg="white",
                                       font=("Times New Roman", 15), command=self.logout)
        self.logout_button.pack(pady=20)

    def display_user_info(self):
        if self.current_user_info and isinstance(self.current_user_info, dict):
            name = self.current_user_info.get("name", "N/A")
            last_name = self.current_user_info.get("last_name", "N/A")
            doctor_id = self.current_user_info.get("doctor_id", "N/A")

            self.name_label = tk.Label(self.profile_frame, text=f"Name: {name} {last_name}", bg="white",
                                       font=("Times New Roman", 20))
            self.name_label.pack()

            self.email_label = tk.Label(self.profile_frame, text=f"Doctor ID: {doctor_id}", bg="white",
                                        font=("Times New Roman", 20))
            self.email_label.pack()
        else:
            self.error_label = tk.Label(self.profile_frame, text="Error: Invalid user information", bg="white",
                                        font=("Times New Roman", 20))
            self.error_label.pack()

    def logout(self):
        self.on_logout()


def create_profile_screen(root, current_user_info, on_logout):
    if current_user_info:
        app = ProfileScreen(root, current_user_info, on_logout)
        root.mainloop()
    else:
        print("Error: No current user information provided.")
