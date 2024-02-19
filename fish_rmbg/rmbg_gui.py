import os
import tkinter as tk
import tkinter.ttk as ttk
from rembg import remove
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageEnhance
from .rmbg import Rmbg
from tqdm import tqdm


class RmbgGUI:

    def __init__(self, master):
        self.master = master
        self.master.title("Fish Background Remover")
        self.input_path = tk.StringVar()
        self.output_path = tk.StringVar()
        self.contrast_value = tk.DoubleVar()
        self.background_color = tk.StringVar(value="transparent") 
        self.progress_bar = ttk.Progressbar(self.master, orient="horizontal", mode="determinate", length=300)
        self.progress_bar.pack(pady=10)
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
        background_color = self.background_color.get()

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

        total_images = len(os.listdir(input_path))
        self.progress_bar["maximum"] = total_images - 1
        self.progress_label = tk.StringVar()

        for image_file in tqdm(image_files):
            input_image_path = os.path.join(input_path, image_file)
            output_image_path = os.path.join(output_path, image_file)

            # image = Image.open(input_image_path)
            # if contrast_value:
            #    enhancer = ImageEnhance.Contrast(image)
            #    image = enhancer.enhance(contrast_value)

            image_bg_rmv = Rmbg().remover(input_image_path, bg_color=background_color)

            output_image_path = os.path.splitext(output_image_path)[0] + "_bg_rmv.png"
            image_bg_rmv.save(output_image_path)

            self.progress_bar["value"] += 1
            self.master.update()

        messagebox.showinfo("Success", "Image processing completed.")
