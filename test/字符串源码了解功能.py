demo = "ZHSNS"
test = "zhsns"
demo1 = "zhsnshcwwyqhxf__"

# start：从那个开始找
# end：找到哪结束

# capitalize()：首字母大写
# v1 = test.capitalize()
# print(v1)

# casefold()、lower():做字母小写转换，但casefold()可以做很多未知特殊字符的变小写的转换。
# v2 = demo.casefold()
# v3 = demo.lower()
# print(v2)
# print(v3)

# center(self, *args, **kwargs):设置宽度并将内容居中
# 第一个参数可以不用，第二个要带参数，第三个不带参数设置为none
# 20：代指总长度
# *：代指空白未知填充，只支持一个字符填充，可有可无
# v4 = test.center(20, "*")
# print(v4)

# count(self, sub, start=None, end=None):去字符串中寻找字符或者是子序列出现的次数
# sub：字符或者是子序列
# v5 = demo1.count("h")
# v6 = demo1.count("h",2,7)
# print(v5)
# print(v6)

# endswith(self, suffix, start=None, end=None)：以什么什么结尾，结果返回布尔值
# startswith(self, suffix, start=None, end=None)：以什么什么开头，结果返回布尔值
# a = demo1.startswith("zh",)
# b = demo1.endswith("zh")
# print(a)
# print(b)

# find(self, sub, start=None, end=None)：从开始往后找，找到第一个后获取其位置
# 结果返回-1就是没找到，找的区间要大于或大于等于该区间。
# v7 = demo1.find("n",4,6)
# # print(v7)

# index(self, sub, start=None, end=None):从开始往后找，找到第一个后获取其位置,与find的区别在于找不到会报错.
# v7 = demo1.index("n")
# print(v7)

# format(self, *args, **kwargs)：格式化，将一个字符串中的占位符替换为指定的值，有点类似传值。
# test1 = "i am {name},age {num}"
# print(test1)
# t = test1.format(name="lulisong",num=19)
# print(t)

# 要替换的位置可以按照出现的顺序替换，下标从0开始。
# test1 = "i am {1},age {0}"
# print(test1)
# t = test1.format("lulisong",19)
# print(t)

# format_map(self, mapping)：同样是格式化替换值，但区别在于传入的值是key_value的形式进行替换，有点像对象数组。
# test1 = "i am {name},age {num}"
# print(test1)
# t = test1.format(name="lulisong",num=22)
# t1 = test1.format_map({"name":"lulisong","num":22})
# print(t)
# print(t1)

# isalnum(self, *args, **kwargs):判断字符串中是否只包含字母和数字. 结果为 true 只包含数字和字母; 结果为 false 也包含其他字符
# t = demo1.isalnum()
# print(t)