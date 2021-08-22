import logging
import os
import shutil
from abc import ABCMeta, abstractmethod
from pathlib import Path

from fileorganizer.file import File


class Action(metaclass=ABCMeta):
    @abstractmethod
    def do(self, file):
        pass


class MoveTo(Action):
    def __init__(self, destination) -> None:
        super().__init__()
        self.__destination = destination

    def do(self, file: File):
        dst_dir = os.path.join(file.enclosing_dir, self.__destination)
        logging.debug(f"move {file.abs_path} to {dst_dir}")
        if not os.path.exists(dst_dir):
            Path(dst_dir).mkdir(parents=True)
        if os.path.isdir(dst_dir):
            shutil.move(file.abs_path, dst_dir)
        else:
            raise RuntimeError(f'{dst_dir} is not a valid directory')
