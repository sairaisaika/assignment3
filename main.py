# -*- coding: utf-8 -*-
# @Time    : 2/27/2020 10:57 PM
# @Author  : WeihaoLiao
# @FileName: main.py
# @Software: PyCharm
from csvReader.csvAction.read_csv import read_csv
from csvReader.csv_controller.csv_controller import csv_controller
from csvReader.dataMap.data_map import data_map

if __name__ == '__main__':
    read_csv()
    csv_controller()