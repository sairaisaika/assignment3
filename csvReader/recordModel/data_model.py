# -*- coding: utf-8 -*-
# @Time    : 2/27/2020 10:57 PM
# @Author  : WeihaoLiao
# @FileName: data_model.py
# @Software: PyCharm
from null import Null

REF_DATE = Null
GEO = Null
DGUID = Null
Age_group = Null
Student_response = Null
UOM = Null
UOM_ID = Null
SCALAR_FACTOR = Null
SCALAR_ID = Null
VECTOR = Null
COORDINATE = Null
VALUE = Null
STATUS = Null
SYMBOL = Null
TERMINATED = Null
DECIMALS = Null


# class moudle object
class data_model:
    def __init__(self, REF_DATE, GEO, DGUID, Sex, Age_group, Student_response, UOM, UOM_ID, SCALAR_FACTOR, SCALAR_ID,
                 VECTOR, COORDINATE, VALUE, STATUS, SYMBOL, TERMINATED, DECIMALS):
        self.REF_DATE = REF_DATE
        self.GEO = GEO
        self.DGUID = DGUID
        self.Sex = Sex
        self.Age_group = Age_group
        self.Student_response = Student_response
        self.UOM = UOM
        self.UOM_ID = UOM_ID
        self.SCALAR_FACTOR = SCALAR_FACTOR
        self.SCALAR_ID = SCALAR_ID
        self.VECTOR = VECTOR
        self.COORDINATE = COORDINATE
        self.VALUE = VALUE
        self.STATUS = STATUS
        self.SYMBOL = SYMBOL
        self.TERMINATED = TERMINATED
        self.DECIMALS = DECIMALS

    # override toString
    def __str__(self):
        return "{}，{}，{}，{}，{}，{}，{}，{}，{}，{}，{}，{}，{}，{}，{}，{}，{}".format(self.REF_DATE, self.GEO, self.DGUID,
                                                                           self.Sex, self.Age_group,
                                                                           self.Student_response, self.UOM, self.UOM_ID,
                                                                           self.SCALAR_FACTOR, self.SCALAR_ID,
                                                                           self.VECTOR, self.COORDINATE, self.VALUE,
                                                                           self.STATUS, self.SYMBOL, self.TERMINATED,
                                                                           self.DECIMALS)

    # getter and setter
    def get_REF_DATE(self):
        return self._REF_DATE

    def set_REF_DATE(self, new_REF_DATE):
        self._REF_DATE = new_REF_DATE

    # getter and setter
    def get_GEO(self):
        return self._GEO

    def set_GEO(self, new_GEO):
        self._GEO = new_GEO

    # getter and setter
    def get_DGUID(self):
        return self._DGUID

    def set_DGUID(self, new_DGUID):
        self.DGUID = new_DGUID

    # getter and setter
    def get_Sex(self):
        return self._Sex

    def set_Sex(self, new_Sex):
        self._Sex = new_Sex

    # getter and setter
    def get_Age_group(self):
        return self._Age_group

    def set_Age_group(self, new_Age_group):
        self._Age_group = new_Age_group

    # getter and setter
    def get_Student_response(self):
        return self._Student_response

    def set_Student_response(self, new_Student_response):
        self._Student_response = new_Student_response

    # getter and setter
    def get_UOM(self):
        return self._UOM

    def set_UOM(self, new_UOM):
        self._UOM = new_UOM

    # getter and setter
    def get_UOM_ID(self):
        return self._UOM_ID

    def set_UOM_ID(self, new_UOM_ID):
        self._UOM_ID = new_UOM_ID

    # getter and setter
    def get_SCALAR_FACTOR(self):
        return self._SCALAR_FACTOR

    def set_SCALAR_FACTOR(self, new_SCALAR_FACTOR):
        self._SCALAR_FACTOR = new_SCALAR_FACTOR

    # getter and setter
    def get_SCALAR_ID(self):
        return self._SCALAR_ID

    def set_SCALAR_ID(self, new_SCALAR_ID):
        self._SCALAR_ID = new_SCALAR_ID

    # getter and setter
    def get_VECTOR(self):
        return self._VECTOR

    def set_VECTOR(self, new_VECTOR):
        self._VECTOR = new_VECTOR

    # getter and setter
    def get_COORDINATE(self):
        return self._COORDINATE

    def set_COORDINATE(self, new_COORDINATE):
        self._COORDINATE = new_COORDINATE

    # getter and setter
    def get_VALUE(self):
        return self._VALUE

    def set_VALUE(self, new_VALUE):
        self._VALUE = new_VALUE

    # getter and setter
    def get_STATUS(self):
        return self._STATUS

    def set_STATUS(self, new_STATUS):
        self._STATUS = new_STATUS

    # getter and setter
    def get_SYMBOL(self):
        return self._SYMBOL

    def set_SYMBOL(self, new_SYMBOL):
        self._SYMBOL = new_SYMBOL

    # getter and setter
    def get_TERMINATED(self):
        return self._TERMINATED

    def set_TERMINATED(self, new_TERMINATED):
        self._TERMINATED = new_TERMINATED

    # getter and setter
    def get_DECIMALS(self):
        return self._DECIMALS

    def set_DECIMALS(self, new_DECIMALS):
        self._DECIMALS = new_DECIMALS
