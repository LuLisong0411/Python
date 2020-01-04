li = [9,5,9,7,2,8,5,3]
# append(self, *args, **kwargs):在原来值后面追加参数
# li.append(5)
# li.append("lulisong")
# li.append([1234])
# print(li)

# clear(self, *args, **kwargs):清空列表
# li.clear()
# print(li)

# copy(self, *args, **kwargs)：拷贝（复制）/浅拷贝
# v = li.copy()
# print(v)

# count(self, *args, **kwargs):计算元素出现的个数
# v = li.count(3)
# print(v)

# extend(self, *args, **kwargs):扩展原来的列表，参数是可迭代对象，内部要执行循环；将参数元素循环加入到原来列表后面
# li.extend([20167108,"lulisong"])
# li.extend("lulisong")
# print(li)

# index(self, *args, **kwargs):根据值获取当前索引位置(左边优先)
# v = li.index(3)
# print(v)

# insert(self, *args, **kwargs):在指定索引位置插入
# li.insert(0,99)
# print(li)

# pop(self, *args, **kwargs):删除某个值，并获取该值（没传参就默认删除最后一个）
# v = li.pop(0)
# print(li)
# print(v)

# remove(self, *args, **kwargs): 删除列表中的指定值，左边优先
# li.remove(3)
# print(li)
#删除方式：pop()、remove、del li[0]、del li[7:9]、clear()

# reverse(self, *args, **kwargs):将当前列表进行反转
# li.reverse()
# print(li)

# sort(self, *args, **kwargs):列表的排序
# 从小到大排序：
# li.sort()
# 从大到小排序：
# li.sort(reverse=True)
# print(li)

