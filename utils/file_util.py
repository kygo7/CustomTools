#!/usr/bin/env python
# encoding: utf-8


import os
from pathlib import Path


class FileUtil(object):
    WORK_DIR = Path(__file__).resolve().parent.parent
    LOG_INI_DIR = os.path.join(WORK_DIR, 'config', 'logging.ini')
    CONFIG_FILE_DIR = os.path.join(WORK_DIR, 'config')
    DATA_DIR = os.path.join(WORK_DIR, 'data')

    @classmethod
    def get_file_full_path(cls, file):
        suffix = os.path.splitext(file)[-1]
        if suffix == 'ini':
            return os.path.join(cls.CONFIG_FILE_DIR, file)
        raise OSError

