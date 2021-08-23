#!/usr/bin/env python3
import argparse

import daemon

from fileorganizer.action import MoveTo
from fileorganizer.actionrunner import ActionRunner
from fileorganizer.folderscanner import FolderScanner
from fileorganizer.rule import ExtensionRule
from fileorganizer.watcher import Watcher

__action_runner = ActionRunner(
    [(ExtensionRule('html'), MoveTo('HTML文件')), (ExtensionRule('zip 7z gzip rar tar gz'), MoveTo('压缩包')),
     (ExtensionRule('doc docx xls xlsx ppt pptx csv'), MoveTo('Office文档')), (ExtensionRule('pdf'), MoveTo('PDF文档')),
     (ExtensionRule('jpg png'), MoveTo('图片')), (ExtensionRule('sh'), MoveTo('可执行脚本')),
     (ExtensionRule('txt'), MoveTo('文本文件')), ])


def start_watcher(watch_path):
    Watcher(watch_path, __action_runner).watch()


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(description='monitor directory and organize files')
    arg_parser.add_argument('Path',
                            metavar='path',
                            type=str,
                            help='the path to watch')
    arg_parser.add_argument('-d',
                            action="store_true",
                            help='run as daemon')
    arg_parser.add_argument('-s',
                            action="store_true",
                            help='perform an initial scan before watch')
    # Execute the parse_args() method
    args = arg_parser.parse_args()
    watch_path = args.Path
    if args.s:
        FolderScanner(watch_path, __action_runner).scan()
    if args.d:
        with daemon.DaemonContext():
            start_watcher(watch_path)
    else:
        start_watcher(watch_path)
