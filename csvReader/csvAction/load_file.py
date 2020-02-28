# -*- coding: utf-8 -*-
# @Time    : 2/27/2020 10:57 PM
# @Author  : WeihaoLiao
# @FileName: load_file.py
# @Software: PyCharm

import os


def load_file():
    # get the current path
    current_path = os.path.abspath(__file__)
    father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")
    config_file_path = os.path.join(os.path.abspath(os.path.dirname(father_path) + os.path.sep + ".."), 'csvFile',
                                    '13100262.csv')
    return config_file_path
