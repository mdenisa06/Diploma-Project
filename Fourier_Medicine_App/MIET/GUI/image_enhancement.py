import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os
import sys
import numpy as np
import cv2
from skimage.metrics import structural_similarity as ssim
from enhanced_image_screen import create_enhanced_photo_screen


class ImageEnhancementScreen:
    def __init__(self, root, current_user_info, on_enhance, on_logout, on_profile):
        self.root = root
        self.root.title("Image Enhancement")
        self.root.geometry("1633x980")
        self.current_user_info = current_user_info
        self.on_enhance = on_enhance
        self.on_logout = on_logout
        self.on_profile = on_profile

        if hasattr(sys, '_MEIPASS'):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.abspath(".")

        background_image_path = os.path.join(base_path, "poza1.png")
        self.background_image = Image.open(background_image_path)
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        self.background_label = tk.Label(root, image=self.background_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.image_frame = tk.Frame(root, bg="white")
        self.image_frame.place(relx=0.5, rely=0.5, anchor="center")

        self.instructions_label = tk.Label(self.image_frame,
                                           text="Click the button to select an image from device.",
                                           bg="white", font=("Times New Roman", 20))
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
                                        font=("Times New Roman", 15), command=self.enhance_image)
        self.enhance_button.grid(row=2, column=2, padx=10, pady=(0, 20), sticky="w")

        self.done_button = tk.Button(self.image_frame, text="Done Enhancing", bg="white",
                                     font=("Times New Roman", 15), command=self.on_profile)
        self.done_button.grid(row=2, column=3, padx=10, pady=(0, 20), sticky="w")

    def browse_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.load_image(file_path)
            self.filename_label.config(text=f"Selected Image: {os.path.basename(file_path)}")
            self.file_path = file_path

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
            enhanced_image = self.apply_adaptive_sharpening(enhanced_image)
            enhanced_image = self.apply_noise_reduction(enhanced_image)

            psnr_value = self.calculate_psnr(self.original_image, enhanced_image)
            print(f"PSNR: {psnr_value:.2f}")

            ssim_value = self.calculate_ssim(self.original_image, enhanced_image)
            print(f"SSIM: {ssim_value:.4f}")

            self.open_enhanced_image_screen(enhanced_image)
        else:
            messagebox.showerror("Error", "Please select an image first.")

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

    def apply_adaptive_sharpening(self, image):
        blurred = cv2.GaussianBlur(image, (5, 5), 10.0)
        return cv2.addWeighted(image, 1.5, blurred, -0.5, 0)

    def apply_noise_reduction(self, image):
        return cv2.medianBlur(image, 3)

    def open_enhanced_image_screen(self, enhanced_image):
        enhanced_image_pil = Image.fromarray(enhanced_image)
        top_level = tk.Toplevel(self.root)
        create_enhanced_photo_screen(top_level, enhanced_image_pil, self.file_path, self.current_user_info,
                                     self.on_enhance, self.on_logout)

    def calculate_psnr(self, original_image, enhanced_image):
        mse = np.mean((original_image - enhanced_image) ** 2)
        if mse == 0:
            return float('inf')
        max_pixel = np.max(original_image)
        psnr = 20 * np.log10(max_pixel / np.sqrt(mse))
        return psnr

    def calculate_ssim(self, original_image, enhanced_image):
        return ssim(original_image, enhanced_image, data_range=enhanced_image.max() - enhanced_image.min())


def create_image_enhancement_screen(root, current_user_info, on_enhance, on_logout, on_profile):
    app = ImageEnhancementScreen(root, current_user_info, on_enhance, on_logout, on_profile)
    root.mainloop()
