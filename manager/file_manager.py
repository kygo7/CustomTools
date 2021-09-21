#!/usr/bin/env python
# encoding: utf-8

from utils.file_util import FileUtil
import shutil
import os
import time


class FileManager(object):
    def __init__(self, source_dir_path, target_dir_path=None):
        self.target_dir_path = target_dir_path if target_dir_path else FileUtil.DATA_DIR
        self.source_dir_path = source_dir_path
        self.source_dir_basename = os.path.basename(self.source_dir_path)

    @property
    def target_master_dir_path(self):
        target_path = os.path.join(self.target_dir_path, self.source_dir_basename)
        if not os.path.exists(target_path):
            os.makedirs(os.path.join(target_path, 'master'))
        return os.path.join(target_path, 'master')

    @property
    def target_backup_dir_path(self):
        target_path = os.path.join(self.target_dir_path, self.source_dir_basename)
        if not os.path.exists(target_path):
            os.makedirs(os.path.join(target_path, 'backup'))
        return os.path.join(target_path, 'backup')

    def push(self):
        shutil.rmtree(self.target_master_dir_path)
        shutil.copytree(self.source_dir_path, os.path.join(self.target_master_dir_path, self.source_dir_basename))

    def backup(self):
        shutil.copytree(self.source_dir_path, os.path.join(self.target_backup_dir_path, str(time.time()),
                                                           self.source_dir_basename))

    @staticmethod
    def get_dir_size(dir_path):
        size = 0
        for root, dirs, files in os.walk(dir_path):
            size += sum([os.path.getsize(os.path.join(root, name)) for name in files])
        return size

    def contrast_dir_size_diff(self):
        return True if self.get_dir_size(self.source_dir_path) == self.get_dir_size(
            self.target_master_dir_path) else False
