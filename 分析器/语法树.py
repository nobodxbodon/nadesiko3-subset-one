import ast

class 语法树:
    @staticmethod
    def 模块(主体):
        return ast.Module(body = 主体)

    @staticmethod
    def 表达式(值):
        return ast.Expr(value = 值, lineno = 1, col_offset = 1)

    @staticmethod
    def 调用(函数):
        return ast.Call(func=函数, lineno = 1, col_offset = 1)

    @staticmethod
    def 名称(标识):
        return ast.Name(id=标识, ctx=ast.Load(), lineno = 1, col_offset = 1)