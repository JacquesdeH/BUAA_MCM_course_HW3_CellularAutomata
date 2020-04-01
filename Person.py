# _*_coding:utf-8_*_
# Author      : JacquesdeH
# Create Time : 2020/3/31 22:55
# Project Name: project
# File        : Person.py
# --------------------------------------------------
import random

from Config import Config
from Status import Status


def infectious(status):
    return status == Status.INCUB or status == Status.SICK


class Person:
    def __init__(self, status=Status.HEALTHY):
        self.status = status

    def infect(self):
        self.status = Status.SICK

    def updateStatus(self, neighbors=None):
        # immune
        if neighbors is None:
            neighbors = []
        if self.status == Status.IMMUNE:
            return
        # sick
        elif self.status == Status.SICK:
            if random.random() < Config.RateHeal:
                self.status = Status.IMMUNE
            if random.random() < Config.RateDeath:
                self.status = Status.NULL
        # incubation
        elif self.status == Status.INCUB:
            if random.random() < Config.RateIncubToSick:
                self.status = Status.SICK
        # healthy
        elif self.status == Status.HEALTHY:
            for neighbor in neighbors:
                if self.status == Status.INCUB:
                    break
                if infectious(neighbor.status) and random.random() < Config.RateInfectByEach:
                    self.status = Status.INCUB
        # dead
        elif self.status == Status.NULL:
            raise ValueError("Dead body has not been dealt with")
        # illegal status
        else:
            raise RuntimeError("Encountered undefined status for Person")

