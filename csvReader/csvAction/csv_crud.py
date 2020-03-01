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
        data_map.view_header("")
        split_sym = []
        orgData = "".join(dataList[self])
        for i in range(len(orgData)):
            if orgData[i] == '，':
                split_sym.append(i)

        print(orgData)

        user_choice = input("which data you want to change? :")
        user_input = input("input the data you want to change: ")

        REF_DATE = orgData[0: split_sym[0]]
        GEO = orgData[split_sym[0] + 1:split_sym[1]]
        DGUID = orgData[split_sym[1] + 1:split_sym[2]]
        Sex = orgData[split_sym[2] + 1:split_sym[3]]
        Age_group = orgData[split_sym[3] + 1:split_sym[4]]
        Student_response = orgData[split_sym[4] + 1:split_sym[5]]
        UOM = orgData[split_sym[5] + 1:split_sym[6]]
        UOM_ID = orgData[split_sym[6] + 1:split_sym[7]]
        SCALAR_FACTOR = orgData[split_sym[7] + 1:split_sym[8]]
        SCALAR_ID = orgData[split_sym[8] + 1:split_sym[9]]
        VECTOR = orgData[split_sym[9] + 1:split_sym[10]]
        COORDINATE = orgData[split_sym[10] + 1:split_sym[11]]
        VALUE = orgData[split_sym[11] + 1:split_sym[12]]
        STATUS = orgData[split_sym[12] + 1:split_sym[13]]
        SYMBOL = orgData[split_sym[13] + 1:split_sym[14]]
        TERMINATED = orgData[split_sym[14] + 1:split_sym[15]]
        DECIMALS = orgData[split_sym[15] + 1:]

        result_list = [REF_DATE, GEO, DGUID, Sex, Age_group, Student_response, UOM, UOM_ID,
                       SCALAR_FACTOR,
                       SCALAR_ID, VECTOR, COORDINATE, VALUE, STATUS, SYMBOL, TERMINATED, DECIMALS]

        position = result_list.index(user_choice)
        result_list[position] = user_input
        str_result_list = "，".join(result_list)
        dataList[self] = str_result_list
        print("You successful change a row, result will show in the next 2 second")
        time.sleep(2)
        data_map.view_list("")
