import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
from PIL import Image, ImageEnhance
from rembg import remove


class FishBGExtractorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Fish Background Remover")

        self.input_path = tk.StringVar()
        self.output_path = tk.StringVar()
        self.contrast_value = tk.DoubleVar()
        self.background_color = tk.StringVar(
            value="transparent"
        )  # Default to transparent
        self.colors_dict = {
            "black": (0, 0, 0, 255),
            "white": (255, 255, 255, 255),
            "blue": (0, 0, 255, 255),
            "navy": (0, 0, 128, 255),
            "green": (0, 128, 0, 255),
            "light_gray": (211, 211, 211, 255),
        }

        self.create_widgets()

    def create_widgets(self):
        # Input Path
        input_frame = tk.Frame(self.master)
        input_frame.pack(pady=10)
        tk.Label(input_frame, text="Input Path:").grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(input_frame, textvariable=self.input_path, width=50).grid(
            row=0, column=1, padx=5, pady=5
        )
        tk.Button(input_frame, text="Browse", command=self.browse_input_path).grid(
            row=0, column=2, padx=5, pady=5
        )

        # Output Path
        output_frame = tk.Frame(self.master)
        output_frame.pack(pady=10)
        tk.Label(output_frame, text="Output Path:").grid(
            row=0, column=0, padx=5, pady=5
        )
        tk.Entry(output_frame, textvariable=self.output_path, width=50).grid(
            row=0, column=1, padx=5, pady=5
        )
        tk.Button(output_frame, text="Browse", command=self.browse_output_path).grid(
            row=0, column=2, padx=5, pady=5
        )

        # Contrast Value
        contrast_frame = tk.Frame(self.master)
        contrast_frame.pack(pady=10)
        tk.Label(contrast_frame, text="Contrast Value:").grid(
            row=0, column=0, padx=5, pady=5
        )
        tk.Entry(contrast_frame, textvariable=self.contrast_value, width=10).grid(
            row=0, column=1, padx=5, pady=5
        )

        # Background Color Selection
        color_frame = tk.Frame(self.master)
        color_frame.pack(pady=10)
        tk.Label(color_frame, text="Background Color:").grid(
            row=0, column=0, padx=5, pady=5
        )
        options = ["black", "gray", "white", "blue", "green", "transparent"]
        tk.OptionMenu(color_frame, self.background_color, *options).grid(
            row=0, column=1, padx=5, pady=5
        )

        # Run Button
        run_button = tk.Button(self.master, text="Run", command=self.process_images)
        run_button.pack(pady=10)

    def browse_input_path(self):
        folder_path = filedialog.askdirectory()
        self.input_path.set(folder_path)

    def browse_output_path(self):
        folder_path = filedialog.askdirectory()
        self.output_path.set(folder_path)

    def process_images(self):
        input_path = self.input_path.get()
        output_path = self.output_path.get()
        contrast_value = self.contrast_value.get()
        background_color = self.colors_dict[self.background_color.get()]

        if not input_path or not output_path:
            messagebox.showerror("Error", "Please select input and output folders.")
            return

        if not os.path.exists(input_path):
            messagebox.showerror("Error", "Input folder does not exist.")
            return

        if not os.path.exists(output_path):
            os.makedirs(output_path)

        image_files = [
            f for f in os.listdir(input_path) if f.endswith((".png", ".jpg", ".jpeg"))
        ]

        for image_file in image_files:
            input_image_path = os.path.join(input_path, image_file)
            output_image_path = os.path.join(output_path, image_file)

            image = Image.open(input_image_path)
            if contrast_value:
                enhancer = ImageEnhance.Contrast(image)
                image = enhancer.enhance(contrast_value)

            image_bg_rmv = remove(image, bgcolor=background_color)

            output_image_path = os.path.splitext(output_image_path)[0] + "_bg_rmv.png"
            image_bg_rmv.save(output_image_path)

        messagebox.showinfo("Success", "Image processing completed.")


def main():
    root = tk.Tk()
    app = FishBGExtractorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
