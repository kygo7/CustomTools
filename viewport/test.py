#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import threading
import time
import os
import shutil


class A(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        shutil.copy(r'D:\MF_Code\UATools\CustomTools\viewport\test.apk',
                    r'D:\MF_Code\UATools\CustomTools\viewport\test.txt.1')


class B(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        x = 0
        y = 0
        if os.path.isfile("test.apk"):
            y = os.stat("test.apk")[6]
        while x < y:
            if os.path.isfile("test.txt.1"):
                x = os.stat("test.txt.1")[6]
            else:
                x = os.stat("test.txt.1")[6]
            b = 0
            a = int((x / y) * 100)
            b = int(a - b)
            j = '#' * int(b / 2)
            print(str(a) + "% ||" + j + "||" + "\r")


def test():
    t1 = A()
    t2 = B()
    t1.start()
    time.sleep(0.1)
    t2.start()


if __name__ == '__main__':
    test()