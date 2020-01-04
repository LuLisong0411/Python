# 元组有序、元组的一级元素不可以被修改、不能被增加或者删除
# 一级元素是列表的话，列表内的元素可以被修改
# 可以索引取值和切片可以被for循环
# 一般在写元组的时候，推荐在最后加个逗号，与参数的形式进行区别
tu = (5,2,3,56,7,89,"20167108","lulisong")
# 索引
# v = tu[0]
# print(v)
# print("-----------------")

# 切片
# v1 = tu[0:3]
# print(v1)
# print("-----------------")

# for 循环：可迭代对象
# for item in tu:
#     print(item)

# count(self, *args, **kwargs): 获取指定元素在元组中出现的次数
# v = tu.count(5)
# print(v)

# index(self, *args, **kwargs)：获取指定元素在元组中的索引
# v = tu.index(56)
# print(v)