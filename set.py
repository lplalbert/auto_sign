# -*- coding: UTF-8 -*- #
"""
@filename :set.py
@author :lplalbert
@time :2022-05-04
"""
import os

path = os.path.split(os.path.abspath(__file__))[0] + "\\run.py"

os.system('schtasks /create /tn "auto_sign" /sc daily /st 02:00:00 /tr ' + path)

#可能会输出乱码，可以忽略

#只需要在第一次使用时运行即可