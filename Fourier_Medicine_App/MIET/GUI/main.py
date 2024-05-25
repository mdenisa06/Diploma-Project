import tkinter as tk
from tkinter import messagebox
from firebase_init import db
from welcome_screen import create_welcome_screen
from login_register_screen import create_login_register_screen
from image_enhancement import ImageEnhancementScreen
from enhanced_image_screen import create_enhanced_photo_screen
from profile_screen import create_profile_screen


class MainApp:
    def __init__(self, root):
        self.current_user_info = None
        self.root = root
        self.show_welcome_screen()

    def show_welcome_screen(self):
        self.clear_screen()
        create_welcome_screen(self.root, self.show_login_register_screen)

    def show_login_register_screen(self):
        self.clear_screen()
        create_login_register_screen(self.root, self.on_login_success)

    def fetch_user_info_from_firestore(self, uid):
        try:
            user_ref = db.collection('users').document(uid)
            user_doc = user_ref.get()
            if user_doc.exists:
                return user_doc.to_dict()
            else:
                print("No such document for UID:", uid)
        except Exception as e:
            print(f"Error fetching user data: {e}")
        return None

    def on_login_success(self, uid):
        if uid:
            fetched_user_info = self.fetch_user_info_from_firestore(uid)
            if fetched_user_info:
                self.current_user_info = fetched_user_info
                self.show_image_enhancement_screen()
            else:
                messagebox.showerror("Error", "Failed to fetch user information from Firestore.")
        else:
            messagebox.showerror("Error", "Invalid UID received after login.")

    def show_image_enhancement_screen(self):
        self.clear_screen()
        ImageEnhancementScreen(self.root, self.current_user_info, self.show_enhanced_image_screen)

    def show_enhanced_image_screen(self, enhanced_image, original_file_path):
        self.clear_screen()
        create_enhanced_photo_screen(self.root, enhanced_image, original_file_path, self.current_user_info)

    def show_profile_screen(self):
        self.clear_screen()
        create_profile_screen(self.root, self.current_user_info)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()


def main():
    root = tk.Tk()
    root.geometry("1633x980")
    app = MainApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
