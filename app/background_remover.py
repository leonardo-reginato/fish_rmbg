import os
import sys
from tqdm import tqdm
from rembg import remove
from PIL import Image, Image, ImageEnhance


def bg_rmv(
    photos_input_dir: str,
    output_dir: str = "",
    contrast_factor: float = None,
    output_ext: str = "png",
) -> bool:
    for filename in tqdm(os.listdir(photos_input_dir)):
        image_path = os.path.join(photos_input_dir, filename)

        # Check if the file is an image
        if not (
            image_path.lower().endswith((".png", ".jpg", ".jpeg", ".nef"))
            and os.path.isfile(image_path)
        ):
            print(f"Skipping {image_path} - not a valid image file.")
            continue

        # Open Image
        image = Image.open(image_path)

        # Enhance contrast
        enhancer = ImageEnhance.Contrast(image)
        if contrast_factor:
            image = enhancer.enhance(contrast_factor)

        # Removing BG
        image_bg_rmv = remove(image)

        # Create output directory
        if output_dir == "":
            output_dir = os.path.join(
                os.path.dirname(os.path.abspath(__file__)) + "/background_remover"
            )

        os.makedirs(output_dir, exist_ok=True)

        # Adjust the image extension to png
        output_file_path = os.path.join(output_dir, "bg_rmv_" + filename)
        output_file_path = os.path.splitext(output_file_path)[0] + "." + output_ext

        # Saving the image
        image_bg_rmv.save(output_file_path)

    return True


if __name__ in "__main__":
    try:
        output = sys.argv[2]
    except:
        output = "../images/background_remover"

    try:
        ctr = int(sys.argv[3])
    except:
        ctr = None

    try:
        output_ext = sys.argv[4]
    except:
        output_ext = "png"

    bg_rmv(
        photos_input_dir=sys.argv[1],
        output_dir=output,
        contrast_factor=ctr,
        output_ext=output_ext,
    )
