import os
from shutil import rmtree
from tempfile import mkdtemp
from typing import Union


def directory():
    return TemporaryDirectory()


class TemporaryDirectory:
    def __enter__(self):
        self.test_dir = mkdtemp()
        return Handle(self.test_dir)

    def __exit__(self, exc_type, exc_val, exc_tb):
        rmtree(self.test_dir)


class Handle:
    def __init__(self, test_dir: str):
        self.test_dir = test_dir

    def store(self, filename: str, content: Union[str, bytes]):
        self.__store_bytes(filename, bytes(content, 'utf-8'))

    def __store_bytes(self, filename: str, bytes_: bytes):
        folder, _ = os.path.split(self.join(filename))
        if not os.path.exists(folder):
            os.makedirs(folder)
        with open(self.join(filename), 'wb') as file:
            file.write(bytes_)

    def open(self, filenames: str) -> str:
        with open(self.join(filenames), 'rb') as file:
            return str(file.read(), 'utf-8')

    def __call__(self, *args, **kwargs) -> str:
        return self.join(*args)

    def join(self, *filenames: str) -> str:
        return os.path.join(self.test_dir, *filenames)