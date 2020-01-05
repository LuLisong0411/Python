# 基本数据类型
# 数字  int 字符串  str    列表   list   元祖   tuple  字典   dict   布尔值     bool
# int 的作用：
#     将字符串转换为数字
a = "123"
print(type(a),a)

b = int(a)
print(type(b),b)

# base = 2, 8, 10, 16转换为相应的进制
num = "0011"
v = int(num,base=2)
print(v)

# age.bit_length()的结果表示当前数字的二进制至少用几位来表示
age = 32
r = age.bit_length()
print(r)
