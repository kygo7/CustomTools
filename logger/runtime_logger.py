#!/usr/bin/env python
# encoding: utf-8

import logging.config
from utils.file_util import FileUtil


class BaseLogger(object):

    def __init__(self, logger_name):
        """
        Constructor
        """
        self.filename = FileUtil.LOG_INI_DIR
        self.logger_name = logger_name
        logging.config.fileConfig(self.filename)
        self.logger = logging.getLogger(self.logger_name)
        pass


runtime_logger = BaseLogger('runtimeLogger')
