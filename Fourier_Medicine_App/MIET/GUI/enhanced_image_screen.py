import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


class EnhancedPhotoScreen:
    def __init__(self, root, enhanced_image):
        self.root = root
        self.root.title("Enhanced Photo")
        self.root.geometry("1633x980")

        self.original_image = enhanced_image
        self.zoom_factor = 1.0

        self.frame = tk.Frame(root, bg="white")
        self.frame.pack(fill="both", expand=True)

        self.canvas_frame = tk.Frame(self.frame, bg="white")
        self.canvas_frame.pack(side=tk.LEFT, fill="both", expand=True)

        self.canvas = tk.Canvas(self.canvas_frame, bg="white")
        self.canvas.pack(fill="both", expand=True)
        self.canvas.bind("<Configure>", self.on_canvas_resize)

        self.display_image()

        self.button_frame = tk.Frame(self.frame, bg="white")
        self.button_frame.pack(side=tk.RIGHT, padx=10, pady=10)

        self.zoom_in_button = tk.Button(self.button_frame, text="Zoom In", command=self.zoom_in, width=10, height=2, bg="white")
        self.zoom_in_button.pack(side=tk.TOP, padx=5, pady=5)

        self.zoom_out_button = tk.Button(self.button_frame, text="Zoom Out", command=self.zoom_out, width=10, height=2, bg="white")
        self.zoom_out_button.pack(side=tk.TOP, padx=5, pady=5)

        self.save_button = tk.Button(self.button_frame, text="Save Photo", command=self.save_photo, width=10, height=2, bg="white")
        self.save_button.pack(side=tk.TOP, padx=5, pady=5)

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
        file_path = filedialog.asksaveasfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.original_image.save(file_path)


def create_enhanced_photo_screen(enhanced_image):
    root = tk.Toplevel()
    app = EnhancedPhotoScreen(root, enhanced_image)
    root.mainloop()


