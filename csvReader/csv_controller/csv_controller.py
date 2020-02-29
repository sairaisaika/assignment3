# -*- coding: utf-8 -*-
# @Time    : 2/27/2020 10:57 PM
# @Author  : WeihaoLiao
# @FileName: csv_controller.py
# @Software: PyCharm
from csvReader.csvAction.csv_crud import *


class csv_controller:
    data_map.view_header("")
    data_map.view_list("")
    while True:
        print("option1: Show all record \n"
              "option2: Create new record \n"
              "option3: Delete record  \n"
              "option4: Select and edit record \n"
              "option5: Exit console application \n")

        try:
            user_input = int(input("which option do you want?(e.g: 1): "))
        except ValueError:
            print("Please inter again \n")
            time.sleep(2)
            break

        while user_input == 1:
            csv_crud.read_list("")
            time.sleep(2)
            break
        while user_input == 2:
            csv_crud.create_row("")
            time.sleep(2)
            break
        while user_input == 3:
            #print("now you want to delete a row, there is " + str(numOfRows) + " rows,")
            input_row = input("Please inter the row you want to delete:")
            if input_row.isdigit():
                num_row = int(input_row) - 1
                csv_crud.delete_row(num_row)
            break
        while user_input == 4:
            csv_crud.update_element()
            break
        while user_input == 5:
            exit()
