import sys
import ast

from 语法树生成 import *
from 木兰.功用.调试辅助 import 语法树相关

源码文件 = sys.argv[1]
with open(源码文件, 'r') as f:
    源码 = f.read()

语法树 = 解析文件(源码)

#print(ast.dump(语法树))
print(语法树相关.格式化节点(语法树, 1))

可执行码 = compile(语法树, 源码文件, 'exec')

exec(可执行码, {})