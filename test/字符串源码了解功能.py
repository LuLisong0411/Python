test = "zhsns"
# capitalize()：首字母大写
v1 = test.capitalize()
print(v1)
print("########################")
# casefold()、lower():做字母小写转换，但casefold()可以做很多未知特殊字符的变小写的转换。
demo = "ZHSNS"
v2 = demo.casefold()
v3 = demo.lower()
print(v2)
print(v3)
print("########################")
# center(self, *args, **kwargs):设置宽度并将内容居中
# 第一个参数可以不用，第二个要带参数，第三个不带参数设置为none
# 20：代指总长度
# *：代指空白未知填充，只支持一个字符填充，可有可无
v4 = test.center(20, "*")
print(v4)
print("########################")
# count(self, sub, start=None, end=None):去字符串中寻找字符或者是子序列出现的次数
# sub：字符或者是子序列
# start：从那个开始找
# end：找到哪结束
demo1 = "zhsnshcwwyqhxf"
v5 = demo1.count("h")
v6 = demo1.count("h",2,7)
print(v5)
print(v6)
print("-----------------------")
# endswith(self, suffix, start=None, end=None)：以什么什么结尾，结果返回布尔值
# startswith(self, suffix, start=None, end=None)：以什么什么开头，结果返回布尔值
# start：从那个开始找
# end：找到哪结束
a = demo1.startswith("zh",)
b = demo1.endswith("zh")
print(a)
print(b)
print("-----------------------")
