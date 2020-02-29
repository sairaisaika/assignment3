# -*- coding: utf-8 -*-
# @Author  : Weihao Liao
# @Time    : 2/28/2020 4:20 AM
# @Function: 
# @FileName: csv_crud.py
# @Software: PyCharm
import time

from csvReader.dataMap.data_map import *
from csvReader.dataMap.data_map import dataList
from csvReader.recordModel.data_model import *


class csv_crud:
    # read list from list
    def read_list(self):
        data_map.view_header(self)
        data_map.view_list(self)

    # create new row in the list
    def create_row(self):
        print("follow the step to insert data(if there is no data you want to put just press space ):")
        new_REF_DATE = input("input REF_DATE: ")
        new_GEO = input("input GEO:")
        new_DGUID = input("input DGUID:")
        new_Sex = input("input Sex:")
        new_Age_group = input("input  Age_group:")
        new_Student_response = input("input Student_response:")
        new_UOM = input("input UOM:")
        new_UOM_ID = input("input UOM_ID:")
        new_SCALAR_FACTOR = input("input SCALAR_FACTOR:")
        new_SCALAR_ID = input("input SCALAR_ID:")
        new_VECTOR = input("input VECTOR:")
        new_COORDINATE = input("input COORDINATE:")
        new_VALUE = input("input VALUE:")
        new_STATUS = input("input STATUS:")
        new_SYMBOL = input("input SYMBOL:")
        new_TERMINATED = input("input VALUE:")
        new_DECIMALS = input("input DECIMALS:")
        model = data_model(new_REF_DATE, new_GEO, new_DGUID, new_Sex, new_Age_group, new_Student_response, new_UOM,
                           new_UOM_ID,
                           new_SCALAR_FACTOR,
                           new_SCALAR_ID, new_VECTOR, new_COORDINATE, new_VALUE, new_STATUS, new_SYMBOL, new_TERMINATED,
                           new_DECIMALS)
        data_map.sort(model.__str__())
        print("You successful create a row, result will show in the next 2 second")
        time.sleep(2)
        data_map.view_list(self)

    # delete row from list
    def delete_row(self):
        dataList.pop(self)
        print("You successful delete a row, result will show in the next 2 second")
        time.sleep(2)
        data_map.view_list(self)

    # update elements from row
    def update_element(self):
        REF_DATE = []
        orgData = dataList[self]
        print("the number " + str(self + 1) + " row is:" + orgData)
        for i in range(len(orgData)):
            if not orgData[i] == '，':
                REF_DATE.append(orgData[i])
            else:
                break

        STRING_REF = "".join(REF_DATE)
        print(STRING_REF)
