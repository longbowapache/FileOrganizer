from abc import ABCMeta, abstractmethod
from typing import List, Union

from fileorganizer.file import File


class Rule(metaclass=ABCMeta):
    @abstractmethod
    def eval(self, file):
        pass


class ExtensionRule(Rule):

    def __init__(self, extensions: Union[List[str], str]) -> None:
        super().__init__()
        if isinstance(extensions, str):
            self.__extension = set(extensions.split(' '))
        else:
            self.__extension = set(extensions)

    def eval(self, file: File):
        return file.extension in self.__extension
