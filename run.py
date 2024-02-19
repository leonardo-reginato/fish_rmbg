import sys
from fish_rmbg import Rmbg


def main(images_input_dir, output_dir, contrast_factor, output_extension):
    Rmbg().remover_from_dir(images_input_dir, output_dir, contrast_factor, output_extension)


if __name__ == "__main__":
    try:
        output = sys.argv[2]
    except:
        output = "./images/rmbg_output"

    try:
        ctr = int(sys.argv[3])
    except:
        ctr = None

    try:
        output_ext = sys.argv[4]
    except:
        output_ext = "png"
        
    main(sys.argv[1], output, ctr, output_ext)
