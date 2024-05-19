import tkinter as tk
from tkinter import filedialog
import numpy as np
from PIL import Image, ImageTk
import cv2
from enhanced_image_screen import create_enhanced_photo_screen


class ImageEnhancementScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Enhancement")
        self.root.geometry("1633x980")

        self.background_image = Image.open("poza1.png")
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        self.background_label = tk.Label(root, image=self.background_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.image_frame = tk.Frame(root, bg="white")
        self.image_frame.place(relx=0.5, rely=0.5, anchor="center")

        self.instructions_label = tk.Label(self.image_frame, text="Drag and drop an image here or click the button to "
                                                                  "select an image from device.", bg="white",
                                           font=("Times New Roman", 20))
        self.instructions_label.grid(row=0, column=0, columnspan=4, pady=20)

        self.padding_label = tk.Label(self.image_frame, bg="white")
        self.padding_label.grid(row=1, column=0, padx=(10, 0))

        self.image_preview_label = tk.Label(self.image_frame, bg="white")
        self.image_preview_label.grid(row=1, column=1, pady=20, sticky="w")

        self.filename_label = tk.Label(self.image_frame, text="", bg="white", font=("Times New Roman", 12))
        self.filename_label.grid(row=1, column=2, pady=20, sticky="w")

        self.select_button = tk.Button(self.image_frame, text="Select Image", bg="white", font=("Times New Roman", 15),
                                       command=self.browse_image)
        self.select_button.grid(row=2, column=1, padx=10, pady=(0, 20), sticky="w")

        self.enhance_button = tk.Button(self.image_frame, text="Enhance Image", bg="white",
                                        font=("Times New Roman", 15),
                                        command=self.enhance_image)
        self.enhance_button.grid(row=2, column=2, padx=10, pady=(0, 20), sticky="w")

    def browse_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.load_image(file_path)
            self.filename_label.config(text=f"Selected Image: {file_path.split('/')[-1]}")

    def load_image(self, file_path):
        image = Image.open(file_path)
        self.original_image = np.array(image)
        if len(self.original_image.shape) == 3:
            self.original_image = cv2.cvtColor(self.original_image, cv2.COLOR_RGB2BGR)

        thumbnail_size = (100, 100)
        image.thumbnail(thumbnail_size)
        self.photo = ImageTk.PhotoImage(image)
        self.image_preview_label.config(image=self.photo)

    def enhance_image(self):
        if hasattr(self, 'original_image'):
            enhanced_image = self.enhance_fourier(self.original_image)
            further_enhanced_image = self.apply_sharpening(enhanced_image)
            self.open_enhanced_image_screen(further_enhanced_image)
        else:
            print("Please select an image first.")

    def enhance_fourier(self, image):

        if len(image.shape) == 3:
            gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            gray_img = image.copy()

        freq_domain = np.fft.fft2(gray_img)

        rows, cols = gray_img.shape
        crow, ccol = rows // 2, cols // 2
        mask = np.ones((rows, cols), np.uint8)
        mask[crow - 30:crow + 30, ccol - 30:ccol + 30] = 0

        freq_domain_filtered = freq_domain * mask

        spatial_domain = np.fft.ifft2(freq_domain_filtered)

        enhanced_img = np.abs(spatial_domain).astype(np.uint8)

        return enhanced_img

    def apply_sharpening(self, image):

        kernel = np.array([[0, -1, 0],
                           [-1, 5, -1],
                           [0, -1, 0]])

        sharpened_img = cv2.filter2D(image, -1, kernel)
        return sharpened_img

    def open_enhanced_image_screen(self, enhanced_image):
        enhanced_image = Image.fromarray(enhanced_image)
        create_enhanced_photo_screen(enhanced_image)


def main():
    root = tk.Tk()
    app = ImageEnhancementScreen(root)
    root.mainloop()


if __name__ == "__main__":
    main()
