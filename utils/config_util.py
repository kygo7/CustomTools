#!/usr/bin/env python
# encoding: utf-8

import configparser
from utils.file_util import FileUtil


class ConfigUtil(object):

    def __init__(self, filename, section_name="root"):
        """
        Constructor
        """
        self.filename = filename
        self.section_name = section_name
        self.config = configparser.ConfigParser()
        self.config.read(self.filename, encoding="utf8")

    def get(self, key, section_name=None):
        section_name = section_name or self.section_name
        return self.config.get(section_name, key)

    def getint(self, key, section_name=None):
        section_name = section_name or self.section_name
        return self.config.getint(section_name, key)

    def getfloat(self, key, section_name=None):
        section_name = section_name or self.section_name
        return self.config.getfloat(section_name, key)

    def getboolean(self, key, section_name=None):
        section_name = section_name or self.section_name
        return self.config.getboolean(section_name, key)

    def get_string_list(self, key, section_name=None):
        section_name = section_name or self.section_name
        value = self.get(key, section_name)
        value_list = value.split(',')
        return [item.strip() for item in value_list]

    def get_int_list(self, key, section_name=None):
        section_name = section_name or self.section_name
        value_list = self.get_string_list(key, section_name)
        return [int(item) for item in value_list]

    def get_float_list(self, key, section_name=None):
        section_name = section_name or self.section_name
        value_list = self.get_string_list(key, section_name)
        return [float(item) for item in value_list]

    def write_ini(self, key, value):
        self.config.set(self.section_name, key, value)
        with open(self.filename, 'w', encoding='utf-8') as f:
            self.config.write(f)
        f.close()


config_singleton = ConfigUtil(FileUtil.get_file_full_path("config.ini"))
