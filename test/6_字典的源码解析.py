# 字典无序、字典是键值对的方式、字典的value可以是任意值、字典的键值对支持del删除、支持for循环
info = {
    "k1":20167108,
    "k2":True,
    "k3":"lulisong",
    True:"232",
    "k4":[
        11,
        (),
        [
            {
                "m1":1,
                "m2":(23,34)
            }
        ]
    ],
    "k5":(12342,345)
}

# 列表、字典不能作为字典的key、其他的可以.
# 布尔值可以作为key、但是要是与其他的key重复，后面的会覆盖前面显示。True 1  Flase 0
# print(info)

# 字典无序，获取字典中的某个值需要逐级往下找
# v = info["k4"][2][0]["m2"][0]
# print(info)
# print(v)

# 键值对的删除  删除"m2"
# del info["k4"][2][0]["m2"]
# print(info)

# for 循环(1)   默认循环所有的key、和for item in info.keys()效果一样
# for item in info:
#     print(item)
# print("----------------")
# for item in info.keys():
#     print(item)

# for 循环(2)   循环value
# for item in info.values():
#     print(item)

# for 循环(3)   循环获取键值对
# for k,v in info.items():
#     print(k,v)

# clear(self):清空字典
# copy(self):浅拷贝

dict = {
    "t1":"x1",
    "t2":"x2",
    "t3":"x3",
}
# fromkeys(*args, **kwargs): 根据序列创建字典、并指定统一的值
# v = dict.fromkeys(["t2",111,"t3"],"sdsd")
# print(v)

# get(self, *args, **kwargs)：根据key获取值，key值不存在时可以指定默认值（None）
# 字典中如果没有键值对会报错
# v1 = dict["ashd"]
# print(v1)

# 字典中如果没有键值对不会报错，会显示None、第二个参数会默认填充代替None；如果有键值对，就忽略不显示第二参数
# v2 = dict.get("sdf")
# v3 = dict.get("sdf","sada")
# v4 = dict.get("t1")
# print(v2)
# print(v3)
# print(v4)

# pop(self, k, d=None):删除键值对，并获取删除的键值对名；如果不存在键值对，不能删除键值对，会把参数默认值返回
# v = dict.pop("t1")
# print(v,v)
# v1 = dict.pop("ksajd",100)
# print(dict,v1)

# popitem(self, *args, **kwargs):随机删除一个键值对，并返回删除的键值对
# k,v = dict.popitem()
# print(dict,k,v)

# setdefault(self, *args, **kwargs):设置值。已存在则不设置、获取当前key对应的值；不存在则设置、获取当前key对应的值
# v = dict.setdefault("asdfas","lulisong")
# v1 = dict.setdefault("t1")
# print(dict,v)
# print(dict,v1)

# update(self, E=None, **F):更新字典的两种方式
# dict.update({"t1":"123","t4":"345"})
# print(dict)
# dict.update(t1=123,t2=2234,t5="asdsa")
# print(dict)

# 字典中最常用的方式：keys()、values()、items()、get()、update()