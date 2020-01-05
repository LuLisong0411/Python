# 运算符   + -  *  /  %  //  **
sum0 = 9 // 2
sum1 = 9 * 2
sum2 = 9 % 2
sum3 = 2 ** 10
print(sum0)
print(sum1)
print(sum2)
print(sum3)
print('------------------')
# 判断某个东西是否在某个东西里包含  in     not in     判断字符串中是否包含子序列
name = '舟杭绍南苏'

if '杭' in name:
    print('第二站')
else:
    print('error')
print('------------------')
if '苏州' not in name:
    print('最后一站')
else:
    print('error')

print('------------------')

# == >= <= !=(不等于) <>(不等于) not(取反)   拿到的结果都是布尔值
# 运算逻辑（执行顺序）：先计算括号里面的，从前到后执行。
# 计算出结果如果是 true 后面遇到 or 就不往后走了，最后结果为 true ，如果遇到 and 继续往后走。
# 如果是 false 遇到 or 继续往后走；如果遇到 and 就不往后走了，结果就为 false。
user = 'root'
pwd = '123'
v = user == 'root' and pwd == '123' or 1==1 and pwd2 == 'root'
print(v)
print('------------------')
# 赋值运算符：+=  -=  //=  %=  *= **=
count0 = 2
count1 = 2
count2 = 10
count3 = 2
count0 += 2
count1 -= 2
count2 %= 2
count3 **= 2
print(count0)
print(count1)
print(count2)
print(count3)

