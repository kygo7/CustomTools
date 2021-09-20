#!/usr/bin/env python
# encoding: utf-8

from ftplib import FTP
from ftplib import error_perm
import os


class FTPUtil(object):
    def __init__(self, ftp_host, ftp_user, ftp_passwd, ftp_port=25):
        self.ftp_host = ftp_host
        self.ftp_user = ftp_user
        self.ftp_passwd = ftp_passwd
        self.ftp_port = ftp_port
        self.ftp = FTP()
        self.ftp.encoding = 'utf-8'
        self.ftp.connect(host=self.ftp_host, port=self.ftp_port)
        self.ftp.login(user=self.ftp_user, passwd=self.ftp_passwd)

    def download_file(self, local_file, remote_file):
        file_handler = open(local_file, "wb")
        ftp_cmd = 'RETR %s' % remote_file  # 这里的命令一定要注意空格不然会说找不到目录
        self.ftp.retrbinary(ftp_cmd, file_handler.write)
        file_handler.close()
        return

    def download_dir(self, local_dir, remote_dir, create_remote_dir_to_local=False):
        """
        :param local_dir: 下载下来的目标路径
        :param remote_dir:  FTP上的目录
        :param create_remote_dir_to_local: 拉取下来的文件没有带远端的目录，为True会在本地创建
        :return:
        """
        if create_remote_dir_to_local:
            _, remote_last_dir_name = os.path.split(remote_dir)
            local_dir = os.path.join(local_dir, remote_last_dir_name)
        if not os.path.isdir(local_dir):
            os.makedirs(local_dir)
        self.ftp.cwd(remote_dir)
        remote_names = self.ftp.nlst()
        for file in remote_names:
            local_file = os.path.join(local_dir, file)
            if self.is_dir(file):
                self.download_dir(local_file, file)
            else:
                pass
                self.download_file(local_file, file)
        self.ftp.cwd("..")
        return

    def is_dir(self, path):
        dir_flag = False

        def show_file_type(line):
            nonlocal dir_flag
            nonlocal path
            if path in line and "drwxr-xr-x" in line:
                dir_flag = True

        self.ftp.retrlines('LIST', show_file_type)
        return dir_flag

    def upload_file(self, local_file, remote_path):
        print(local_file, remote_path)
        file_handle = open(local_file, 'rb')
        ftp_cmd = 'STOR %s' % remote_path
        self.ftp.storbinary(ftp_cmd, file_handle)

    def upload_dir(self, local_dir, remote_dir):
        try:
            self.ftp.mkd(remote_dir)
        except error_perm:  # 这里表示文件存在550 File exists.
            pass
        for i in os.listdir(local_dir):
            file = os.path.join(local_dir, i)
            if os.path.isdir(file):
                self.upload_dir(file, remote_dir + '/' + i)
            else:
                self.upload_file(file, remote_dir + '/' + i)

    def close(self):
        self.ftp.quit()
        self.ftp.close()


if __name__ == '__main__':
    pass
