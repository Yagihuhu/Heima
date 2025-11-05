# age = 25
# if age >= 18:
#     print("happy")
#
#     print("go go")
#
# print("看看什么时间会执行")

# age = int(input("输入年龄:"))
#
# if age >= 18:
#     print("happy")
#
# else:
#     print("no no")
#
# print("看看什么时间会执行")

# age = 120
# if age >= 0 and age <= 120:
#     print("年龄正确")
#
# else:
#     print("年龄错误")

# A = 50
# B = 16
#
# if A > 60 or B > 60:
#     print("通过")
#
# else:
#     print("不通过")

# is_student = True  #条件是true

# 一般想要条件不成立时，使用该方法
# if not is_student:
#     print("条件不成立执行：不是本校学生不能进入")   #输出
#
# else:
#     print("条件成立执行：是本校学生，可以进入")


# a = 1
# while a < 5 :
#     print(a)
#     a += 2

# my_list = [1, 2, 3, 4, 5]
# # 移除并返回最后一个元素
# last_element = my_list.pop()
# print(last_element)  # 输出：5
# print(my_list)       # 输出：[1, 2, 3, 4]
#
# # 移除并返回索引为 1 的元素
# second_element = my_list.pop(1)
# print(second_element)  # 输出：2
# print(my_list)         # 输出：[1, 3, 4]

# continue 和 break 用法

# i = 1
# while i < 10:
#     i += 1
#     if i % 2 > 0:  # 非双数时跳过输出
#         continue
#     print (i)# 输出双数2、4、6、8、10

# holiday_name = "生日"
# if holiday_name == "情人节":
#     print('买花')
# elif holiday_name == "生日":
#     print('买蛋糕')
# elif holiday_name == "平安夜":
#     print('买苹果')
#
# else:
#     print('每天都是节日')


# has_ticket = True
# k_length = 30
# if has_ticket:
#     print("车票检查通过，进行安检")
#     if k_length > 20:
#         print("长的长度为%d，不符合要求，不能上车" % k_length)
#
# else:
#     print("请买票")

#石头剪刀布
# import random
# player = int(input("请输入要出的拳，石头1，剪刀2，布3 :"))
#
# computer = random.randint(1,3)
#
# print("玩家出的是 %d 电脑出的是 %d" % (player,computer))
#
# #玩家胜
# #石头 胜 剪刀
# #剪刀 胜 布
# #布 胜 石头
#
# if (player == 1 and computer == 2) \
#         or (player == 2 and computer == 3) \
#         or (player == 3 and computer == 1):
#
#     print("玩家胜")
#
# elif player == computer:
#
#     print("平局")
#
# else:
#
#     print("电脑胜")



