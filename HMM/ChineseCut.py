# -*- coding: utf-8 -*-
__author__ = 'ShadowWalker'
from Viterbi import *
import os

# 测试算法
BaseDir = os.path.dirname(__file__)
# print(BaseDir)
#ChineseCut(BaseDir+"\\PKU_GB\\pku_test.txt", BaseDir+ "\\PKU_GB\\pku_test_result.txt")
# ChineseCutStr("如果真的数据库被物理删除，那么干这事的人，一定能访问到数据的物理文件。")
# ChineseCutStr("我是中国科学院大学的学生，现在研一。")
ChineseCutStr(u"这篇文章写得太平淡了")

