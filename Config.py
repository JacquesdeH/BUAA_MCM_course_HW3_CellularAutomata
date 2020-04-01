# _*_coding:utf-8_*_
# Author      : JacquesdeH
# Create Time : 2020/3/31 23:06
# Project Name: project
# File        : Config.py
# --------------------------------------------------

class Config:
    SEED = 7

    T = 0.01  # refresh period
    TotalRefreshCnt = 300  # cnt of simulation lasting
    # total simulation time = T * TotalRefreshCnt

    N_ROW = 166
    N_COLUMN = 101

    RateHeal = 0.3
    RateInfectBySICK = 0.3
    RateInfectByINCUB = 0.3
    RateIncubToSick = 0.1
    RateDeath = 0.1

    Population = 1000
