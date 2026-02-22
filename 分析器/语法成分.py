from enum import Enum, unique

@unique
class 语法(Enum):
    模块 = '模块'
    语句 = '语句'
    表达式 = '表达式'
    赋值语句 = '赋值语句'
    输出语句 = '输出语句'
    名称 = '名称'
    常量 = '常量'

    def 成分(self, *所有成分):
        文本 = []
        for 成分 in 所有成分:
            if isinstance(成分, Enum):
                文本.append(成分.name)
            else:
                文本.append(成分)
        return self.name + " : " + " ".join(文本)
