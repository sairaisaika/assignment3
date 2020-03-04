# -*- coding: utf-8 -*-
# @Time    : 2/27/2020 10:57 PM
# @Author  : WeihaoLiao
# @FileName: data_map.py
# @Software: PyCharm


n = 17
dataList = []
dataHeader = []

# data map is the class define the list and data header also the action on map
class data_map:
    # user to sort datalist
    def sort(self):
        dataList.append(self)
    # the header getter is just use to get the header one scv first read, user can not change it
    def set_Header(self):
        dataHeader.append(self)
    # show header
    def view_header(self):
        for i in range(len(dataHeader) - 1):
            print(dataHeader[i], end=' ')
        print(' ')
    # use to view list(count is use to count how many row in the list, haven't any function reach this yet
    def view_list(self):
        count = 0
        for i in range(len(dataList)):
            print(dataList[i], end='\n')
            count += 1
