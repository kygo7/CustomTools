#!/usr/bin/env python
# encoding: utf-8

from tkinter import Tk, StringVar, Label, Entry, Button
from tkinter.filedialog import askdirectory
from manager.file_manager import FileManager


class BaseViewPort(object):
    def __init__(self):
        self.tk = Tk()
        self.tk.title('My CustomTools')
        self.source_entry = StringVar()
        self.target_entry = StringVar()

    def set_windows_size(self, x: int, y: int):
        self.tk.geometry(f'{x}x{y}')

    def run(self):
        self.tk.mainloop()

    def panel(self):
        Label(self.tk, text='同步&备份路径').grid(row=0, column=0)
        Entry(self.tk, textvariable=self.source_entry).grid(row=0, column=1)
        Button(self.tk, text='路径选择', command=self.load_path).grid(row=0, column=2)
        Button(self.tk, text='Push', command=self.push).grid(row=0, column=3)
        Button(self.tk, text='BackUp', command=None).grid(row=0, column=4)
        ''''''
        Label(self.tk, text='拉取路径').grid(row=1, column=0)
        Entry(self.tk, textvariable=self.target_entry).grid(row=1, column=1)
        Button(self.tk, text='Pull', command=None).grid(row=1, column=2)
        ''''''
        Button(self.tk, text='查询记录', command=None).grid(row=2, column=0)

    def load_path(self):
        filename = askdirectory()
        self.source_entry.set(filename)

    def get_path(self):
        return self.source_entry.get()

    def push(self):
        source_dir_path = self.get_path()
        fm = FileManager(source_dir_path)
        fm.push()


a = BaseViewPort()
a.panel()
print(a.run())
