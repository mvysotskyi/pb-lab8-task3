"""
GrayscaleADT module.
"""

import numpy as np

from PIL import Image, ImageOps
from lzw import LZW

class GrayscaleImage:
    """
    Represents a grayscale image.
    """
    def __init__(self, nrows: int, ncols: int):
        self.nrows = nrows
        self.ncols = ncols
        self.image_grayscale = np.zeros((nrows, ncols), dtype=np.uint8)

        self.lzw_instance = LZW()

    def __str__(self):
        return str(self.image_grayscale)

    def from_file(self, filename: str, shape_overwrite: bool = False):
        """
        Reads the image from the file and stores it in the ADT.
        """
        image = Image.open(filename)
        image_grayscale = ImageOps.grayscale(image)

        if shape_overwrite:
            self.ncols, self.nrows = image_grayscale.size
            self.image_grayscale = np.zeros((self.nrows, self.ncols), dtype=np.uint8)

        self._load_to_array_2d(image_grayscale)

    def to_file(self, filename: str):
        """
        Writes the image stored in the ADT to the file.
        """
        image = Image.fromarray(self.image_grayscale)
        image.convert("RGB").save(filename)

    def _load_to_array_2d(self, pil_image: Image) -> np.array:
        """
        Converts a PIL Image object to a 2D array.
        """
        for i in range(self.nrows):
            for j in range(self.ncols):
                try:
                    self.image_grayscale[i, j] = pil_image.getpixel((j, i))
                except IndexError:
                    ...

    def lzw_compression(self, dest: str) -> tuple[int, int]:
        """
        Compresses the image using the LZW algorithm.
        """
        compressed = self.lzw_instance.compress(self.image_grayscale.flatten())
        LZW.to_file(compressed, dest)

        return len(compressed), 2

    def lzw_decompression(self, src: str):
        """
        Decompresses the image using the LZW algorithm.
        """
        compressed = LZW.from_file(src)
        decompressed = self.lzw_instance.decompress(compressed)

        self.image_grayscale = np.array(decompressed).reshape(self.nrows, self.ncols)

    def getitem(self, row: int, col: int) -> int:
        """
        Returns the value of the element at position [i, j].
        """
        return self.image_grayscale[row, col]

    def setitem(self, row: int, col: int, value: int):
        """
        Sets the value of the element at position [i, j] to value.
        """
        assert value >= 0 and value <= 255, "Value must be between 0 and 255"
        self.image_grayscale[row, col] = value

    def clear(self, value: int):
        """
        Clears the image by setting each pixel to the given value.
        """
        assert value >= 0 and value <= 255, "Value must be between 0 and 255"
        self.image_grayscale.fill(value)

    def width(self) -> int:
        """
        Returns the number of columns in the image.
        """
        return self.ncols

    def height(self) -> int:
        """
        Returns the number of rows in the image.
        """
        return self.nrows
