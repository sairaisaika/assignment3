# -*- coding: utf-8 -*-
# @Time    : 2/27/2020 10:57 PM
# @Author  : WeihaoLiao
# @FileName: load_file.py
# @Software: PyCharm

import os


def load_file():
    # 获取当前文件路径
    current_path = os.path.abspath(__file__)
    # 获取当前文件的父目录
    father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")
    father_path_2 = os.path.abspath(os.path.dirname(father_path) + os.path.sep + ".")
    config_file_path1 = os.path.join(os.path.abspath(os.path.dirname(father_path_2) + ".."), '13100262.csv')
