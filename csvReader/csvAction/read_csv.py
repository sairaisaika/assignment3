# -*- coding: utf-8 -*-
# @Time    : 2/27/2020 10:57 PM
# @Author  : WeihaoLiao
# @FileName: read_csv.py
# @Software: PyCharm

import csv
from csvReader.recordModel.data_model import data_model

file = "C://Users/saira/PycharmProjects/assignment3/csvFile/13100262.csv"


class read_csv:
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

            moudle = dataModel(REF_DATE, GEO, DGUID, Sex, Age_group, Student_response, UOM, UOM_ID, SCALAR_FACTOR,
                               SCALAR_ID, VECTOR, COORDINATE, VALUE, STATUS, SYMBOL, TERMINATED, DECIMALS)

            print(moudle)
