import tkinter as tk
from tkinter import filedialog
import numpy as np
from scipy.fft import fft2, ifft2, fftshift, ifftshift
from PIL import Image, ImageTk
import cv2


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
                                                                  "select an image.", bg="white", font=("Times New "
                                                                                                        "Roman", 20))
        self.instructions_label.grid(row=0, column=0, columnspan=2, pady=20)

        self.image_preview_label = tk.Label(self.image_frame, bg="white")
        self.image_preview_label.grid(row=1, column=0, columnspan=2, pady=20)

        self.select_button = tk.Button(self.image_frame, text="Select Image", bg="white", font=("Times New Roman", 15),
                                       command=self.browse_image)
        self.select_button.grid(row=2, column=0, padx=10)

        self.enhance_button = tk.Button(self.image_frame, text="Enhance Image", bg="white",
                                        font=("Times New Roman", 15), command=self.enhance_image)
        self.enhance_button.grid(row=2, column=1, padx=10)

    def browse_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.load_image(file_path)

    def load_image(self, file_path):
        image = Image.open(file_path)
        self.original_image = np.array(image)
        if len(self.original_image.shape) == 3:
            self.original_image = cv2.cvtColor(self.original_image, cv2.COLOR_RGB2BGR)
        self.photo = ImageTk.PhotoImage(image)
        self.image_preview_label.config(image=self.photo)

    def enhance_image(self):
        if hasattr(self, 'original_image'):
            enhanced_image = self.enhance_fourier(self.original_image)
            self.display_enhanced_image(enhanced_image)
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

    def display_enhanced_image(self, enhanced_image):
        enhanced_image = Image.fromarray(enhanced_image)
        self.enhanced_photo = ImageTk.PhotoImage(enhanced_image)
        self.image_preview_label.config(image=self.enhanced_photo)


def main():
    root = tk.Tk()
    app = ImageEnhancementScreen(root)
    root.mainloop()


if __name__ == "__main__":
    main()
