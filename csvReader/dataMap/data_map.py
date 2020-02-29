# -*- coding: utf-8 -*-
# @Time    : 2/27/2020 10:57 PM
# @Author  : WeihaoLiao
# @FileName: data_map.py
# @Software: PyCharm


from null import Null


n = 17
dataList = []
dataHeader = []
numOfRows = Null

class data_map:

    def sort(self):
        dataList.append(self)

    def set_Header(self):
        dataHeader.append(self)

    def view_header(self):
        for i in range(len(dataHeader) - 1):
            print(dataHeader[i], end=' ')
        print(' ')

    def view_list(self):
        count = 0
        for i in range(len(dataList)):
            print(dataList[i], end='\n')
            count += 1

        #get_rows_count(count)
