import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os
from firebase_admin import auth
from profile_screen import create_profile_screen


class EnhancedPhotoScreen:
    def __init__(self, root, enhanced_image, original_file_path, current_user_info):
        self.root = root
        self.root.title("Enhanced Photo")
        self.root.geometry("1633x980")
        self.original_image = enhanced_image
        self.original_file_path = original_file_path
        self.current_user_info = current_user_info
        self.zoom_factor = 1.0

        self.frame = tk.Frame(root, bg="black", relief=tk.RAISED)
        self.frame.pack(fill="both", expand=True)

        # Canvas Frame
        self.canvas_frame = tk.Frame(self.frame, bg="black", relief="sunken")
        self.canvas_frame.pack(side=tk.LEFT, fill="both", expand=True, padx=10, pady=10)

        self.canvas = tk.Canvas(self.canvas_frame, bg="black")
        self.canvas.pack(fill="both", expand=True)
        self.canvas.bind("<Configure>", self.on_canvas_resize)

        self.display_image()
        # Button Frame
        self.button_frame = tk.Frame(self.frame, bg="black")
        self.button_frame.pack(side=tk.LEFT, padx=10, pady=10, fill="y")

        self.zoom_in_button = tk.Button(self.button_frame, text="Zoom In", command=self.zoom_in, width=15, height=2,
                                        bg="white", fg="black")
        self.zoom_in_button.pack(side=tk.TOP, padx=5, pady=5)

        self.zoom_out_button = tk.Button(self.button_frame, text="Zoom Out", command=self.zoom_out, width=15, height=2,
                                         bg="white", fg="black")
        self.zoom_out_button.pack(side=tk.TOP, padx=5, pady=5)

        self.save_button = tk.Button(self.button_frame, text="Save Photo", command=self.save_photo, width=15, height=2,
                                     bg="white", fg="black")
        self.save_button.pack(side=tk.TOP, padx=5, pady=5)

        self.profile_button = tk.Button(self.button_frame, text="Profile", command=self.open_profile_screen, width=15,
                                        height=2, bg="white", fg="black")
        self.profile_button.pack(side=tk.TOP, padx=5, pady=5)

    def on_canvas_resize(self, event):
        self.display_image()

    def display_image(self):
        width = int(self.original_image.width * self.zoom_factor)
        height = int(self.original_image.height * self.zoom_factor)
        x = (self.canvas.winfo_width() - width) // 2
        y = (self.canvas.winfo_height() - height) // 2

        resized_image = self.original_image.resize((width, height))
        self.tk_image = ImageTk.PhotoImage(resized_image)
        self.canvas.delete("all")
        self.canvas.create_image(x, y, anchor="nw", image=self.tk_image)

    def zoom_in(self):
        self.zoom_factor *= 1.2
        self.display_image()

    def zoom_out(self):
        self.zoom_factor /= 1.2
        self.display_image()

    def save_photo(self):
        folder_path = r"C:\Users\Denisa\Desktop\Diploma Project\Diploma-Project\Fourier_Medicine_App\MIET\Enhancement Results"
        os.makedirs(folder_path, exist_ok=True)

        file_name = os.path.basename(self.original_file_path)
        enhanced_image_path = os.path.join(folder_path, f"enhanced_{file_name}")
        self.original_image.save(enhanced_image_path)
        messagebox.showinfo("Image Saved", f"Enhanced image saved as {enhanced_image_path}")

    def open_profile_screen(self):
        if self.current_user_info:
            root_profile = tk.Toplevel(self.root)
            create_profile_screen(root_profile, self.current_user_info)
        else:
            messagebox.showerror("Error", "No user logged in.")


def create_enhanced_photo_screen(root, enhanced_image, original_file_path, current_user_info):
    app = EnhancedPhotoScreen(root, enhanced_image, original_file_path, current_user_info)
    root.mainloop()
