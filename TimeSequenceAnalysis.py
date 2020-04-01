# _*_coding:utf-8_*_
# Author      : JacquesdeH
# Create Time : 2020/4/1 11:43
# Project Name: project
# File        : TimeSequenceAnalysis.py
# --------------------------------------------------

from Status import Status

def drawTimeSequenceGraph(seq=None):
    if seq is None:
        seq = [{Status.HEALTHY: 20}]
    raise NotImplementedError("Time Sequence")
