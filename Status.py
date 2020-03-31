# _*_coding:utf-8_*_
# Author      : JacquesdeH
# Create Time : 2020/3/31 22:32
# Project Name: project
# File        : Status.py
# --------------------------------------------------

from enum import Enum

class Status(Enum):
    WALL = -1
    NULL = 0
    HEALTHY = 1
    INCUB = 2
    SICK = 3
    IMMUNE = 4
