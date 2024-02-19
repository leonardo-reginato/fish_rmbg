import os
import sys
from tqdm import tqdm
from rembg import remove
from PIL import Image, ImageEnhance


class Rmbg:
    def __init__(self, contrast_factor=None):
        self.contrast_factor = contrast_factor
        self.colors_dict = {
            "black": (0, 0, 0, 255),
            "white": (255, 255, 255, 255),
            "blue": (0, 0, 255, 255),
            "navy": (0, 0, 128, 255),
            "green": (0, 128, 0, 255),
            "gray": (211, 211, 211, 255),
            "transparent": (0, 0, 0, 0),
        }

    def remover(self, image_path:str, contrast_factor=None, bg_color="transparent") -> Image:
        img = Image.open(image_path)
        if contrast_factor or self.contrast_factor:
            enhance = ImageEnhance.Contrast(img)
            factor = contrast_factor or self.contrast_factor
            img = enhance.enhance(factor)

        # Removing BG
        img_bg_rmv = remove(img, bgcolor=self.colors_dict[bg_color])
        return img_bg_rmv

    def remover_from_dir(
        self,
        images_input_dir:str,
        output_dir:str="",
        contrast_factor:float=None,
        output_extension:str="png",
    ) -> None:
        """
        Function to remove background from all images in a directory
        """

        for filename in tqdm(os.listdir(images_input_dir)):
            image_path = os.path.join(images_input_dir, filename)

            # Check if the file is an image
            if not (
                image_path.lower().endswith((".png", ".jpg", ".jpeg", ".nef"))
                and os.path.isfile(image_path)
            ):
                print(f"Skipping {image_path} - not a valid image file.")
                continue

            img_bg_rmv = self.remover(image_path, contrast_factor)

            if not output_dir:
                output_dir = os.path.join(
                    os.path.dirname(os.path.abspath(__file__)), "output_rmbg"
                )

            os.makedirs(output_dir, exist_ok=True)

            output_file_path = os.path.join(output_dir, "rmgb_" + filename)
            output_file_path = (
                os.path.splitext(output_file_path)[0] + "." + output_extension
            )
            img_bg_rmv.save(output_file_path)
