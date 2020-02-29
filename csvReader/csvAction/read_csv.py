# -*- coding: utf-8 -*-
# @Time    : 2/27/2020 10:57 PM
# @Author  : WeihaoLiao
# @FileName: read_csv.py
# @Software: PyCharm
import re
import csv
from csvReader.recordModel.data_model import *
from csvReader.csvAction.load_file import *
from csvReader.dataMap.data_map import *

# get the csv file path
file = load_file()


class read_csv:


    # if the row have number return 2, use to defined if there is not data column
    def check_num(self):
        pattern = re.compile('[0-9]+')
        for v in self:
            match = pattern.findall(v)
            if match:
                return 1
            else:
                return 2

    # The Simple function to read the file
    with open(file, 'r', encoding='utf-8-sig') as ifile:
        read = csv.reader(ifile)
        a = read.__next__()
        for c in a:
            # print the colum name
            print(c, end=" ")
            # print my name
        print("Weihao Liao")

        # loop to read teh csv file and give to the private variables
        for row in read:
            result = check_num(row)
            if result == 1:
                REF_DATE = row[0]
                GEO = row[1]
                DGUID = row[2]
                Sex = row[3]
                Age_group = row[4]
                Student_response = row[5]
                UOM = row[6]
                UOM_ID = row[7]
                SCALAR_FACTOR = row[8]
                SCALAR_ID = row[9]
                VECTOR = row[10]
                COORDINATE = row[11]
                VALUE = row[12]
                STATUS = row[13]
                SYMBOL = row[14]
                TERMINATED = row[15]
                DECIMALS = row[16]

                model = data_model(REF_DATE, GEO, DGUID, Sex, Age_group, Student_response, UOM, UOM_ID, SCALAR_FACTOR,
                                   SCALAR_ID, VECTOR, COORDINATE, VALUE, STATUS, SYMBOL, TERMINATED, DECIMALS)

                data_map.sort(model.__str__())
                print(model)
