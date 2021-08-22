import logging
from unittest import TestCase

from fileorganizer.action import MoveTo
from fileorganizer.folderscanner import FolderScanner
from fileorganizer.rule import ExtensionRule


class TestFolderScanner(TestCase):
    def test_scan(self):
        logging.basicConfig(level=logging.DEBUG)
        scanner = FolderScanner("~/Desktop", [
            (ExtensionRule('html'), MoveTo('HTML文件')),
            (ExtensionRule('zip 7z gzip rar tar gz'), MoveTo('压缩包')),
            (ExtensionRule('doc docx xls xlsx ppt pptx csv'), MoveTo('Office文档')),
            (ExtensionRule('pdf'), MoveTo('PDF文档')),
            (ExtensionRule('jpg png'), MoveTo('图片')),
            (ExtensionRule('sh'), MoveTo('可执行脚本')),
            (ExtensionRule('txt'), MoveTo('文本文件')),
        ])
        scanner.scan()
