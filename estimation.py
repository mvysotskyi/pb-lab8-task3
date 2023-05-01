"""
Module to esmitate compression ratio of LZW algorithm.
"""

from grayscaleadt import GrayscaleImage

def main(image_path: str):
    """
    Main function.
    """
    image = GrayscaleImage(0, 0)

    try:
        image.from_file(image_path, shape_overwrite=True)
        image.to_file("output.png")
    except FileNotFoundError:
        print("File not found.")
        exit(1)

    size, code_size = image.lzw_compression("test.lzw")

    print(f"Compressed Size: {size * code_size} bytes")
    print(f"Original size: {image.height() * image.width()} bytes")

if __name__ == "__main__":
    image_path = input("Enter image path: ")
    main(image_path)
