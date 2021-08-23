import os
import pathlib


class File():
    def __init__(self, folder, filename) -> None:
        super().__init__()
        self.__filename = filename
        self.__folder = folder

    @property
    def abs_path(self):
        return os.path.join(self.__folder, self.__filename)

    @property
    def extension(self):
        return pathlib.Path(self.abs_path).suffix[1:]

    @property
    def enclosing_dir(self):
        return self.__folder

    def __str__(self) -> str:
        return self.abs_path


