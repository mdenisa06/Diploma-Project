import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


class FourierTransformScreen:
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
        image = image.resize((300, 300), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(image)
        self.image_preview_label.config(image=self.photo)

    def enhance_image(self):
        pass


def main():
    root = tk.Tk()
    app = FourierTransformScreen(root)
    root.mainloop()


if __name__ == "__main__":
    main()
