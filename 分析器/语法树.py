import ast
from rply import 词
from rply.词 import 字符位置

from 分析器.语法成分 import 语法

class 语法树:

    @staticmethod
    def 节点(
            类型, 主体=None, 值=None, 标识=None, 函数=None, 各参数=None,
            变量=None, 片段=None):
        if 类型 == 语法.模块:
            节点 = ast.Module(body = 主体)
        elif 类型 == 语法.表达式:
            节点 = ast.Expr(value = 值)
        elif 类型 == 语法.常量:
            节点 = ast.Constant(value = 值)
        elif 类型 == 语法.名称:
            节点 = ast.Name(id=标识, ctx=ast.Load())
        elif 类型 == 语法.输出语句:
            节点 = ast.Call(func=函数, args=各参数)
        elif 类型 == 语法.赋值语句:
            变量.ctx = ast.Store()
            节点 = ast.Assign(targets=[变量], value=值)

        if 片段 is not None:
            节点.lineno = 语法树.取行号(片段)
            节点.col_offset = 语法树.取列号(片段)
        else: # 如`块`转化为条件语句，片段信息不保留
            节点.lineno = 0
            节点.col_offset = 0
        return 节点

    @staticmethod
    def 取源码位置(片段):
        if isinstance(片段, list):
            if len(片段) > 0:
                片段 = 片段[0]
        if isinstance(片段, 词):
            return 片段.getsourcepos()
        if isinstance(片段, ast.Name) or isinstance(片段, ast.Expr) or isinstance(片段, ast.Constant):
            return 字符位置(0, 片段.lineno, 片段.col_offset)
        信息 = ""
        if 'lineno' in 片段:
            信息 += f"需第{片段.lineno}行"
        if 'col_offset' in 片段:
            信息 += f"第{片段.col_offset}列的"
        信息 += f"长度为{len(片段)}的{str(type(片段))}的位置"
        raise Exception(信息)

    @staticmethod
    def 取行号(片段):
        return 语法树.取源码位置(片段).lineno

    @staticmethod
    def 取列号(片段):
        return 语法树.取源码位置(片段).colno