import unittest

from pathlib import Path

from 语法树生成 import *
from 木兰.功用.调试辅助 import 语法树相关

语法树目录 = Path("测试/语法树/")

class test所有(unittest.TestCase):

    def test(self):
        所有对照语法树 = list(语法树目录.glob('**/*.txt'))
        总用例数 = len(所有对照语法树)
        当前序号 = 1
        for 完整路径 in 所有对照语法树:
            with open(完整路径, 'r', encoding='utf-8') as f:
                目标语法树 = f.read()

            文件名 = str(完整路径)[:-len(完整路径.suffix)]
            木兰路径 = 文件名 + ".ul日"
            with open(木兰路径, 'r', encoding='utf-8') as f:
                源码 = f.read()
                语法树 = 解析文件(源码)
                语法树输出 = 语法树相关.格式化节点(语法树, 1)
            
            print(f"{当前序号}/{总用例数} {文件名}")
            self.assertEqual(语法树输出, 目标语法树, 木兰路径 + " 转换错误")
            当前序号 += 1