# Background Remover Application

This Python application utilizes the `rembg`, `PIL`, and `tqdm` libraries to remove the background from a set of images. It enhances the contrast of the images before removing the background to improve the overall result.

## Requirements
```bash
python: >3.7, <3.12
```

## Installation
1. Clone the repository:
```bash
git clone https://github.com/LeonardoFonsecaR7/fish_background_remover.git
```
2. Navigate to the project directory:
```bash
cd fish_background_remover/
```
3. Before running the application, ensure you have the required libraries installed. You can install them using the following command:
```bash
pip install -r requirements.txt
```
The requirements installation will make sure that you have [rembg library](https://github.com/danielgatis/rembg) installed as it is not included in the standard Python libraries.

## Usage
4. Navigate to the project directory:
```bash
cd app/
```
3. Run the application:
```bash
python background_remover.py [photos_input_dir] [output_dir] [contrast_factor]
```

- [photos_input_dir]: Path to the directory containing the images to process.
- [output_dir] (optional): Path to the directory where the processed images will be saved. If not provided, the default is the "/images/background_remover/" directory inside the project folder.
- [contrast_factor] (optional): A floating-point number representing the contrast enhancement factor. Default is NONE.
4. Example:
```bash
python background_remover.py ../images/original_photos ../images/background_remover 1.5
```
This command will process images in the "../images/original_photos" directory, save the output in the "../images/background_remover", and use a contrast enhancement factor of 1.5.

**Note**: The processed images will be saved in PNG format with a filename prefix "bg_rmv_."

## License 
This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.
