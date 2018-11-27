import re 
pattern="[a-zA-Z]+://[^\s]*[.com|.cn]"
string="<a herf='http://www.baidu.com'>百度首页</a>"
result=re.search(pattern,string)
print(result) 