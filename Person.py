# _*_coding:utf-8_*_
# Author      : JacquesdeH
# Create Time : 2020/3/31 22:55
# Project Name: project
# File        : Person.py
# --------------------------------------------------

from Config import Config
from Status import Status

class Person:
    def __init__(self, status=Status.HEALTHY):
        self.status = status

    def updateStatus(self, neighbors=None):
        pass
