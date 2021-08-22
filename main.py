import argparse

from fileorganizer.action import MoveTo
from fileorganizer.actionrunner import ActionRunner
from fileorganizer.rule import ExtensionRule
from fileorganizer.watcher import Watcher

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(description='monitor directory and organize files')
    arg_parser.add_argument('Path',
                            metavar='path',
                            type=str,
                            help='the path to watch')
    # Execute the parse_args() method
    args = arg_parser.parse_args()
    watch_path = args.Path
    Watcher(watch_path,
            ActionRunner([
                (ExtensionRule('html'), MoveTo('HTML文件')),
                (ExtensionRule('zip 7z gzip rar tar gz'), MoveTo('压缩包')),
                (ExtensionRule('doc docx xls xlsx ppt pptx csv'), MoveTo('Office文档')),
                (ExtensionRule('pdf'), MoveTo('PDF文档')),
                (ExtensionRule('jpg png'), MoveTo('图片')),
                (ExtensionRule('sh'), MoveTo('可执行脚本')),
                (ExtensionRule('txt'), MoveTo('文本文件')),
            ])
            ).watch()
