# _*_coding:utf-8_*_
# Author      : JacquesdeH
# Create Time : 2020/3/31 23:06
# Project Name: project
# File        : Config.py
# --------------------------------------------------

class Config:
    SEED = 7

    T = 0.2  # refresh period
    TotalRefreshCnt = 100  # cnt of simulation lasting
    # total simulation time = T * TotalRefreshCnt

    N = 300

    RateHeal = 0.2
    RateInfectByEach = 0.2
    RateIncubToSick = 0.3
    RateDeath = 0.1

    Population = 500
