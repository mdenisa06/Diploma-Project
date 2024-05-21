import tkinter as tk
from PIL import Image, ImageTk
from firebase_admin import firestore


class ProfileScreen:
    def __init__(self, root, uid):
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

        # Fetch user information
        self.user_info = self.get_user_info(uid)
        if self.user_info:
            name = self.user_info.get("name", "N/A")
            last_name = self.user_info.get("last_name", "N/A")
            doctor_id = self.user_info.get("doctor_id", "N/A")

            self.name_label = tk.Label(self.profile_frame, text=f"Name: {name} {last_name}", bg="white",
                                       font=("Times New Roman", 20))
            self.name_label.pack()

            self.email_label = tk.Label(self.profile_frame, text=f"Doctor ID: {doctor_id}", bg="white",
                                        font=("Times New Roman", 20))
            self.email_label.pack()

            self.phone_label = tk.Label(self.profile_frame, text="Hospital Department: Neurology", bg="white",
                                        font=("Times New Roman", 20))
            self.phone_label.pack()
        else:
            self.name_label = tk.Label(self.profile_frame, text="Error fetching profile information", bg="white",
                                       font=("Times New Roman", 20))
            self.name_label.pack()

        self.logout_button = tk.Button(self.profile_frame, text="Logout", bg="white",
                                       font=("Times New Roman", 15), command=self.logout)
        self.logout_button.pack(pady=20)

    def get_user_info(self, uid):
        try:
            db = firestore.client()
            user_ref = db.collection('users').document(uid)
            user_doc = user_ref.get()
            if user_doc.exists:
                return user_doc.to_dict()
            else:
                print("No such document.")
                return None
        except Exception as e:
            print(f"Error fetching user data: {e}")
            return None


def create_profile_screen(user_id):
    root = tk.Tk()
    app = ProfileScreen(root, user_id)
    root.mainloop()
