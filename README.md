# pb-lab8-task3
Task 3 from Lab 8 for PB(UCU)

## Task
In this task we have to create class **GrayscaleADT** to work and manipulate with grayscale images.

## Installation
Clone the repository and install the dependencies using the following command:

```bash
$ pip install -r requirements.txt
```

## GrayscaleImage

The `GrayscaleImage` class represents a grayscale image and provides methods for reading, writing, compressing, and decompressing the image. 

### Constructor

```python
def __init__(self, nrows: int, ncols: int)
```

Creates a new `GrayscaleImage` object with a given number of rows and columns.

### Methods

#### `from_file(filename: str, shape_overwrite: bool = False) -> None`

Reads the image from the file and stores it in the ADT. If `shape_overwrite` is set to `True`, the size of the image will be overwritten by the size of the loaded image.

#### `to_file(filename: str) -> None`

Writes the image stored in the ADT to the file.

#### `_load_to_array_2d(pil_image: Image) -> np.array`

Converts a PIL Image object to a 2D array.

#### `lzw_compression(dest: str) -> Tuple[int, int]`

Compresses the image using the LZW algorithm and writes it to a file. Returns a tuple containing the size of the compressed data and the compression ratio.

#### `lzw_decompression(src: str) -> None`

Decompresses the image using the LZW algorithm from a file.

#### `getitem(row: int, col: int) -> int`

Returns the value of the element at position `[i, j]`.

#### `setitem(row: int, col: int, value: int) -> None`

Sets the value of the element at position `[i, j]` to `value`.

#### `clear(value: int) -> None`

Clears the image by setting each pixel to the given `value`.

#### `width() -> int`

Returns the number of columns in the image.

#### `height() -> int`

Returns the number of rows in the image.

## LZW

The `LZW` class provides static methods for compressing and decompressing a sequence of 8-bit integers using LZW compression over an 8-bit alphabet.

### Methods

#### `compress(data: List[int]) -> List[int]`
Compresses the given data using LZW compression. Returns a tuple containing the compressed data.

#### `decompress(data: List[int]) -> List[int]`
Decompresses the given data using LZW compression.

## estimate.py

The `estimate.py` script is used to estimate the compression ratio of the LZW algorithm for different images.
Example of usage:

```bash
$ python estimate.py
Enter image path: test.jpg
Compressed Size: 11512410 bytes
Original size: 16163840 bytes
```