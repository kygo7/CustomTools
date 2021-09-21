#!/usr/bin/env python
# encoding: utf-8
import time
from tkinter import Tk, StringVar, Label, Entry, Button, Message
from tkinter.filedialog import askdirectory
from manager.file_manager import FileManager
import threading


class BaseViewPort(object):
    def __init__(self):
        self.tk = Tk()
        self.tk.title('My CustomTools')
        self.source_entry = StringVar()
        self.target_entry = StringVar()
        self.message = StringVar()
        self.update_interval = 100    # 默认100s
        self.auto_path_flag = False

    def set_windows_size(self, x: int, y: int):
        self.tk.geometry(f'{x}x{y}')

    def run(self):
        self.tk.mainloop()

    def panel(self):
        Label(self.tk, text='同步&备份路径').grid(row=0, column=0)
        Entry(self.tk, textvariable=self.source_entry).grid(row=0, column=1)
        Button(self.tk, text='路径选择', command=self.select_source_path).grid(row=0, column=2)
        Button(self.tk, text='Push', command=self.push).grid(row=0, column=3)
        Button(self.tk, text='BackUp', command=self.backup).grid(row=0, column=4)
        ''''''
        Label(self.tk, text='拉取&目标路径').grid(row=1, column=0)
        Entry(self.tk, textvariable=self.target_entry).grid(row=1, column=1)
        Button(self.tk, text='路径选择', command=self.select_target_path).grid(row=1, column=2)
        Button(self.tk, text='Pull', command=None).grid(row=1, column=3)
        ''''''
        Button(self.tk, text='自动监控文件&同步', command=self.threading_auto_push).grid(row=2, column=0)
        Label(self.tk, text='监控频率(s)', command=None).grid(row=2, column=1)
        Entry(self.tk, textvariable=self.update_interval).grid(row=2, column=2)
        Button(self.tk, text='查询记录', command=None).grid(row=3, column=0)
        Message(self.tk, textvariable=self.message).grid(row=4, rowspan=4, columnspan=4)

    def select_source_path(self):
        filename = askdirectory()
        self.source_entry.set(filename)

    def select_target_path(self):
        filename = askdirectory()
        self.target_entry.set(filename)

    def get_source_path(self):
        return self.source_entry.get()

    def get_target_path(self):
        return self.target_entry.get()

    def push(self):
        source_dir_path = self.get_source_path()
        target_dir_path = self.get_target_path()
        fm = FileManager(source_dir_path, target_dir_path)
        fm.push()
        self.message.set(f'{time.time()} --- push file success')
        del fm

    def backup(self):
        source_dir_path = self.get_source_path()
        target_dir_path = self.get_target_path()
        fm = FileManager(source_dir_path, target_dir_path)
        fm.backup()
        self.message.set(f'{time.time()} --- backup file success')
        del fm

    def threading_auto_push(self):
        self.auto_path_flag = ~self.auto_path_flag      # 点击了一次开关 取反
        self.message.set('开启自动同步' if self.auto_path_flag else '关闭自动同步')
        source_dir_path = self.get_source_path()
        target_dir_path = self.get_target_path()
        fm = FileManager(source_dir_path, target_dir_path)

        def auto_push():
            while self.auto_path_flag:
                if not fm.contrast_dir_size_diff():
                    fm.push()
                time.sleep(self.update_interval)
        t = threading.Thread(target=auto_push)
        t.start()
