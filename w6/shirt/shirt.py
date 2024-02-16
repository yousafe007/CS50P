import sys
import os.path
from PIL.ImageOps import fit
from PIL import Image
def main():

    if not correct_args_num():
        sys.exit("Two command line arguments required")

    before = sys.argv[1]
    after = sys.argv[2]

    if not file_exists(before):
        sys.exit(f'Could not read {before}')
    # if not file_exists(file2):
    #     sys.exit(f'Invalid Output')

    if not are_image_files(before, after):
        sys.exit("Not an Image file!")


    shirt = Image.open("shirt.png")
    before_image = Image.open(before)

    resized_before_image= fit(before_image, shirt.size)
    resized_before_image.paste(shirt, shirt)

    resized_before_image.save(after)


def correct_args_num():
    if len(sys.argv) == 3:
        return True

def are_image_files(f1: str, f2:str):
    _, ext1 = os.path.splitext(f1)
    _, ext2 = os.path.splitext(f2)
    return (ext1 == ext2) and (ext1.lower() in ['.jpg' ,'.jpeg', '.png'])

def file_exists(file: str):
    return os.path.isfile(file)

if __name__ == '__main__':
    main()
