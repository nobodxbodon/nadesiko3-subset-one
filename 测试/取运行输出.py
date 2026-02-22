import sys
from io import StringIO
from pathlib import Path

from 语法树生成 import *

def 运行算法(源码文件):
    源码文件 = str(Path(源码文件))
    with open(源码文件, 'r', encoding='utf-8') as f:
        源码 = f.read()

    语法树 = 解析文件(源码)

    # 参考： https://stackoverflow.com/questions/3906232/python-get-the-print-output-in-an-exec-statement
    原标准输出 = sys.stdout

    # 默认换行符为 \n，见 https://docs.python.org/zh-cn/3.7/library/io.html#io.StringIO
    重定向输出 = sys.stdout = StringIO()

    # 参考：https://docs.python.org/3.7/library/functions.html?highlight=compile#compile
    try:
        可执行码 = compile(语法树, 源码文件, 'exec')

        exec(可执行码, {})
    except Exception as e:
        return e
    finally:
        sys.stdout = 原标准输出

    return 重定向输出.getvalue()
