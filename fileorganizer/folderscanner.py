import logging
import os

from fileorganizer.actionrunner import ActionRunner
from fileorganizer.file import File


class FolderScanner():

    def __init__(self, folder_path, action_runner: ActionRunner) -> None:
        super().__init__()
        self.__folder_path = os.path.expanduser(folder_path)
        self.__action_runner = action_runner

    def scan(self):
        files = [File(self.__folder_path, f) for f in os.listdir(self.__folder_path) if
                 os.path.isfile(os.path.join(self.__folder_path, f))]
        for file in files:
            self.__organize(file)

    def __organize(self, file: File):
        logging.debug(f"process {file.abs_path}")
        self.__action_runner.eval(file)
