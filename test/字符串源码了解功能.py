demo = "ZHSNS"
test = "zhsns"
demo1 = "zhsnshcwwyqhxf"
test1 = "i am {name},age {num}"
test2 = "username\temail\tpassword\nlulisong\tlulisong@qq.com\t12345678\nlulisong\tlulisong@qq.com\t12345678\n"

# start：从那个开始找
# end：找到哪结束

# capitalize()：首字母大写
# v1 = test.capitalize()
# print(v1)

# casefold()、lower():做字母小写转换，但casefold()可以做很多未知特殊字符的变小写的转换。
# swapcase(self, *args, **kwargs)：将字符串做大写转换
# v2 = demo.casefold()
# v3 = demo.lower()
# v4 = demo1.swapcase()
# print(v2)
# print(v3)
# print(v4)

# center(self, *args, **kwargs):设置宽度并将内容居中
# ljust(self, *args, **kwargs)：设置宽度将内容放在左边
# rjust(self, *args, **kwargs)：设置宽度将内容放在右边
# zfill(self, *args, **kwargs)：设置宽度将内容放在右边，默认只能用0填充
# 第一个参数可以不用，第二个要带参数，第三个不带参数设置为none
# 20：代指总长度
# *：代指空白未知填充，只支持一个字符填充，可有可无
# v4 = test.center(20, "*")
# v5 = test.ljust(20,"*")
# v6 = test.rjust(20."*")
# v7 = test.zfill(20)
# print(v4)
# print(v5)
# print(v6)
# print(v7)

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

# expandtabs(self, *args, **kwargs)：按给的参数断句，断句遇见有\t的话补空格，补到和参数一样长度，\n的话就换行。可以做表格
# v = test2.expandtabs(30)
# print(v)

# isalpha(self, *args, **kwargs)：判断字符串是否是字母,汉字
# t = demo.isalpha()
# print(t)

# isdecimal(self, *args, **kwargs)：判断一个字符串是否是数字，不支持特殊字符，中文数字
# isdigit(self, *args, **kwargs)：判断一个字符串是否是数字，支持特殊字符，不支持中文数字
# isnumeric(self, *args, **kwargs)：判断一个字符串是否是数字，包含中文数字
# testStr = "②"
# testStr = "123"
# v1 = test.isdecimal()
# v2 = test.isdigit()
# print(v1,v2)

# isidentifier(self, *args, **kwargs)：判断是否是标识符，def,数字，字母，下划线
# test3 = "_123"
# v = test3.isidentifier()
# print(v)

# isprintable(self, *args, **kwargs)：是否存在不可显示的字符
# test3 = "odfujsojf\tkasjhdkas"
# v = test3.isprintable()
# print(v)

# isspace(self, *args, **kwargs)：判断是否全部是空格
# test3 = "    "
# v = test3.isspace()
# print(v)

# istitle(self, *args, **kwargs)：判断是否是标题
# title(self, *args, **kwargs)：把一个字符串转换成标题
# test3 = "Return True if the string is a title-cased string, False otherwise."
# v = test3.istitle()
# v1 = test3.title()
# v2 = v1.istitle()
# print(v)
# print(v1)
# print(v2)

# join(self, ab=None, pq=None, rs=None)：将字符串中的每一个元素按照指定的分割符进行拼接。
# test3 = "舟杭绍南苏"
# print(test3)
# t = " "
# v = t.join(test3)
# v1 = "_".join(test3)
# print(v)
# print(v1)

# islower(self, *args, **kwargs)：判断字符串是否全为小写
# isupper(self, *args, **kwargs)：判断字符串是否全为大写
# v = test.islower()
# v1 = test.isupper()
# print(v,v1)

# 移除指定匹配，有限最多匹配
# lstrip(self, *args, **kwargs)
# rstrip(self, *args, **kwargs)
# strip(self, *args, **kwargs)
# v = demo1.lstrip("zh")
# v1 = demo1.rstrip("sn")
# v2 = demo1.strip("asd")
# print(v,v1,v2)

# 创建一个对应关系，一一替换
# maketrans(self, *args, **kwargs)
# translate(self, *args, **kwargs)
# v = "saoaeioasxasaourad"
# m = str.maketrans("aiueo","12345")
# new_v = v.translate(m)
# print(new_v)

# partition(self, *args, **kwargs)：从左往右只能分割为三份，按匹配到的第一个分割
# rpartition(self, *args, **kwargs)：从右往左只能分割为三份，按匹配到的第一个分割
# split(self, *args, **kwargs)：从左往右分割，不包含分割的参数，可以设置分割的参数来分割份数
# rsplit(self, *args, **kwargs)：从右往左分割，不包含分割的参数，可以设置分割的参数来分割份数
# test3 = "askjdsaklsjdfasoifda"
# v = test3.partition("s")
# v1 = test3.rpartition("3")
# v2 = test3.split("s")
# v3 = test3.rsplit("s",2)
# print(v)
# print(v1)
# print(v2)
# print(v3)

# splitlines(self, *args, **kwargs)：分割只能根据True,False 来保留是否换行字符。
# test3 = "asdjhajkh\nsdkja\nasdfas"
# v = test3.splitlines(False)
# v1 = test3.splitlines(True)
# print(v)
# print(v1)
