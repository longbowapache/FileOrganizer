import logging
import os
from typing import List, Tuple

from fileorganizer.action import Action
from fileorganizer.file import File
from fileorganizer.rule import Rule


class FolderScanner():

    def __init__(self, folder_path, rule_to_action: List[Tuple[Rule, Action]]) -> None:
        super().__init__()
        self.__folder_path = os.path.expanduser(folder_path)
        self.__rule_to_action = rule_to_action

    def scan(self):
        files = [File(self.__folder_path, f) for f in os.listdir(self.__folder_path) if
                 os.path.isfile(os.path.join(self.__folder_path, f))]
        for file in files:
            self.__organize(file)

    def __organize(self, file: File):
        logging.debug(f"process {file.abs_path}")
        for rule_action in self.__rule_to_action:
            rule = rule_action[0]
            action = rule_action[1]
            if rule.eval(file):
                action.do(file)
