from 分析器.词法 import 分词器
from 分析器.语法 import 分析器

def 解析文件(源码):
    各词 = 分词器.分词(源码)
    return 分析器.按语法分词(各词)