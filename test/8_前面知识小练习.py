# 一、有两个列表li1 = [1,3,4,5,7,8,9]、li2 = [1,2,4,6,8,3]
# li1 = [1,3,4,5,7,8,9]
# li2 = [1,2,4,6,8,3]
# (1)获取内容相同的元素
# for i in li1:
#     if i in li2:
#         print(i)

# (2)获取li1中有，li2中没有的元素
# for i in li1:
#     if i not in li2:
#         print(i)

# (3)获取li2中有，li1中没有的元素
# for i in li2:
#     if i not in li1:
#         print(i)

# (4)获取li1和li2中不同的元素
# for i in li1:
#     if i not in li2:
#         print(i)
# for i in li2:
#     if i not in li1:
#         print(i)

# 二、有1、2、3、4、5、6、7、8八个数字，能组成多少个互不相同且无重复数字的两位数
# 方法一：缺点是数字多的话，不知道重复的有多少
# count = 0
# for i in range(1,9):
#     for j in range(1,9):
#         count += 1
# count = count - 8
# print(count)
# 方法二：弥补了方法一的缺陷
# count = 0
# # for i in range(1,9):
# #     for j in range(1,9):
# #         if i != j:
# #             count += 1
# # print(count)
# 方法三：通过遍历索引
count = 0
# li = [1,2,3,4,5,6,7,8]
# for i in range(0,len(li)):
#     for j in range(0,len(li)):
#         if i != j:
#             count += 1
# print(count)
# 方法四:分区间遍历
# count = 0
# li = [1,2,3,4,5,6,7,8]
# l = len(li)
# for i in range(0,l-1):
#     for j in range(i+1,l):
#             count += 2
# print(count)

# 三、打印九九乘法表
# 方法一:
# for i in range(1,10):
#     string = ""
#     for j in range(1,i+1):
#         string += str(j)+"*"+str(i)+"="+str(i*j)+"\t"
#     print(string)
# 方法二:利用print()的end参数默认值是\n实现换行
# for i in range(1,10):
#     for j in range(1,i+1):
#           print(str(j)+"*"+str(i)+"="+str(i*j)+"\t",end="")
#     print("\n",end="")

# 四、Python开发自动计算
#     笔记本5元一本、圆珠笔3元一支、笔芯1元三支，用100元买100样文具用品，其中三样东西都必须要有、
# 请问各类物品要各买多少刚好用完100元？
# 方法一：执行效率低
# for i in range(1,100):
#     for j in range(1,100):
#         for k in range(1,100):
#             if i+j+k==100 and i*5+j*3+k/3==100:
#                 print(i,j,k)
# 方法二：提高了执行效率，//是除法取整
# for i in range(1,100//5):
#     for j in range(1,100//3):
#         for k in range(1,100):
#             if i+j+k==100 and i*5+j*3+k/3==100:
#                 print(i,j,k)

# 五、有一个列表li = [2,7,1,8,6,3,585,4,5],请找到列表中任意两个元素相加和为9的元素集合和索引，如[(1,8),(4,5)]
# li = [2,7,1,8,6,3,585,4,5]
# newLi = []
# indexLi = []
# 元素集合
# for i in li:
#     for j in li:
#         if i+j==9:
#             newLi.append((i,j))
# print(newLi)
# 索引集合
# for indeI in range(0,len(li)):
#     for indexJ in range (0,len(li)):
#         if li[indeI]+li[indexJ]==9:
#             indexLi.append((indeI,indexJ))
# print(indexLi)

# 六、分页显示内容
# （1）通过for循环创建301条数据，内容不限，如：
# lulisong-1      lulisong1@show.com       pwd1
# lulisong-2      lulisong2@show.com       pwd2
# lulisong-3      lulisong3@show.com       pwd3
# ......
# (2)提示用户，请输入要查看的页码，当用户输入指定页码，则显示指定数据。
# 每页显示10条数据、用户输入的是非十进制数字，则提示输入内容格式错误
user_list = []
for i in range(1,302):
    temp = {
        "name":"lulisong-"+str(i),
        "email":"lulisong"+str(i)+"@show.com",
        "pwd":"pwd"+str(i)
    }
    user_list.append(temp)
# print(user_list)
# 每页显示10条数据
s = input("请输入页码：")
s = int(s)
# 某页的起始数据
start = (s-1)*10
end  = s*10
result = user_list[start:end]
for item in result:
    print(item,type(item))
