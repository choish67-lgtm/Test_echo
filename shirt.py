import sys
from PIL import Image, ImageOps

def main():
    if len(sys.argv) < 3:
        sys.exit("Too Few Command-line Argument!")
    elif len(sys.argv) > 3:
        sys.exit("Too Many Command-line Argument!")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    valid_extensions = [".jpg", ".jpeg", ".png"]
    input_ext = get_extension(input_file)
    output_ext = get_extension(output_file)

    if input_ext not in valid_extensions:
        sys.exit("Invalid Input Extension!")
    if output_ext not in valid_extensions:
        sys.exit("Invalid Output Extension!")
    
    if input_ext != output_ext:
        sys.exit("Input and Output must have the same Extension!")

    process(input_file, output_file)
    

def get_extension(filename):
    return "." + filename.rsplit(".", 1)[-1].lower()

def process(input_file, output_file):
    try:
        input_image = Image.open(input_file)
        shirt = Image.open("shirt.png")
        input_image = ImageOps.fit(input_image, shirt.size)
        input_image.paste(shirt, mask=shirt)
        input_image.save(output_file)
    except FileNotFoundError:
        sys.exit("Input File does not exist!")

if __name__ == "__main__":
    main()


