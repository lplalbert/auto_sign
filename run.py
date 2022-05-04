# -*- coding: UTF-8 -*- #
"""
@filename :run.py
@author :lplalbert
@time :2022-05-04
"""
import os

path = os.path.split(os.path.abspath(__file__))[0] + "\\auto_sign.py"

os.system('python '+ path)