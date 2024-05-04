from tkinter import Tk, Button, Label, filedialog
from converter import ImageConverter

class ImageConverterGUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("Img2webp")

        self.root.geometry("300x200")
        self.root.resizable(False, False)

        self.input_folder = ""
        self.output_folder = ""

        self.input_folder_label = Label(self.root, text="Input Folder:")
        #  add top margin
        self.input_folder_label.pack(
            pady=5
        )

        self.output_folder_label = Label(self.root, text="Output Folder:")
        self.output_folder_label.pack(
            pady=5
        )

        self.input_button = Button(self.root, text="Select Input Folder", command=self.select_input_folder)
        self.input_button.pack(
            pady=5
        )

        self.output_button = Button(self.root, text="Select Output Folder", command=self.select_output_folder)
        self.output_button.pack(
            pady=5
        )

        # put convert button a little below more
        self.convert_button = Button(self.root, text="Convert", command=self.convert_images)
        self.convert_button.pack(
            pady=20
        )

    def select_input_folder(self):
        self.input_folder = filedialog.askdirectory()
        self.input_folder_label.config(text=f"Input Folder: {self.input_folder}")

    def select_output_folder(self):
        self.output_folder = filedialog.askdirectory()
        self.output_folder_label.config(text=f"Output Folder: {self.output_folder}")

    def convert_images(self):
        converter = ImageConverter(self.input_folder, self.output_folder)
        converter.convert_images()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = ImageConverterGUI()
    app.run()
