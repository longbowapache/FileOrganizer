import logging
from typing import List, Tuple

from fileorganizer.action import Action
from fileorganizer.file import File
from fileorganizer.rule import Rule


class ActionRunner():
    def __init__(self, rule_to_action: List[Tuple[Rule, Action]]) -> None:
        super().__init__()
        self.__rule_to_action = rule_to_action

    def eval(self, file: File):
        for rule_action in self.__rule_to_action:
            rule = rule_action[0]
            action = rule_action[1]
            if rule.eval(file):
                action.do(file)
                logging.info(f'perform {action} on file {file}')
