#!/usr/bin/env python
# encoding: utf-8

from utils.file_util import FileUtil
import shutil
import os


class FileManager(object):
    def __init__(self, source_dir_path):
        self.target_dir_path = FileUtil.DATA_DIR
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
        target_path = os.path.join(self.target_dir_path,  self.source_dir_basename)
        if not os.path.exists(target_path):
            os.makedirs(os.path.join(target_path, 'backup'))
        return os.path.join(target_path, 'backup')

    def push(self):
        shutil.rmtree(self.target_master_dir_path)
        shutil.copytree(self.source_dir_path, os.path.join(self.target_master_dir_path, self.source_dir_basename))

    def backup(self):
        shutil.copytree(self.source_dir_path, os.path.join(self.target_backup_dir_path, self.source_dir_basename))

