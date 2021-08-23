import logging
import os
import time

from watchdog.events import FileSystemEventHandler, FileCreatedEvent
from watchdog.observers import Observer

from fileorganizer.actionrunner import ActionRunner
from fileorganizer.file import File


class FileEventHandler(FileSystemEventHandler):

    def __init__(self, base_dir, action_runner: ActionRunner):
        super().__init__()
        self.__action_runner = action_runner
        self.__base_dir = base_dir

    def on_created(self, event):
        if isinstance(event, FileCreatedEvent):
            self.__action_runner.eval(File(self.__base_dir, os.path.basename(event.src_path)))


class Watcher:
    def __init__(self, directory, action_runner: ActionRunner) -> None:
        super().__init__()
        self.__directory = os.path.expanduser(directory)
        self.__event_handler = FileEventHandler(self.__directory, action_runner)

    def watch(self):
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S')
        logging.info(f"start to watch {self.__directory}")
        observer = Observer()
        observer.schedule(self.__event_handler, self.__directory, recursive=False)
        observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()
