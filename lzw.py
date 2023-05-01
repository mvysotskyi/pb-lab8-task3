"""
LZW algorithm implementation.
"""

class LZW:
    """
    LZW algorithm implementation.
    """
    def __init__(self):
        self._init_dictinary = {chr(i): i for i in range(256)}

    def compress(self, data: list[int]) -> list[int]:
        """
        Compress data using LZW algorithm.
        """
        dictionary = self._init_dictinary.copy()
        result = []
        word = ""

        for char in data:
            wordc = word + chr(char)

            if wordc in dictionary:
                word = wordc
            else:
                result.append(dictionary[word])
                if len(dictionary) < 65530:
                    dictionary[wordc] = len(dictionary)
                word = chr(char)

        if word:
            result.append(dictionary[word])

        return result

    def decompress(self, data: list[int]) -> list[int]:
        """
        Decompress data using LZW algorithm.
        """
        dictionary = {value: key for key, value in self._init_dictinary.items()}

        result = []
        word = chr(data[0])
        result.append(data[0])

        for k in data[1:]:
            if k in dictionary:
                entry = dictionary[k]
            elif k == len(dictionary):
                entry = word + word[0]
            else:
                raise ValueError(f"Bad compressed k: {k}")

            result.extend([ord(c) for c in entry])
            dictionary[len(dictionary)] = word + entry[0]
            word = entry

        return result

    @staticmethod
    def to_file(compressed: list[int], path: str):
        """
        Write data to file.
        """
        with open(path, "wb") as fpointer:
            for code in compressed:
                fpointer.write(code.to_bytes(2, byteorder="big"))

    @staticmethod
    def from_file(path: str) -> list[int]:
        """
        Read compressed data from file and returns decompressed codes sequence.
        """
        data = []

        with open(path, "rb") as fpointer:
            while True:
                code = fpointer.read(2)
                if not code:
                    break
                data.append(int.from_bytes(code, byteorder="big"))

        return data
