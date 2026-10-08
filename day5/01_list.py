#01_list.py
my_list = [2,5,8,11]
#索引、切片
print(my_list[0])
print(my_list[-1])
print(my_list[1:3])

#增
my_list.append(14)
my_list.extend([17,20])
my_list.insert(1, 99)

#sort原地修改；sorted返回新列表
nums = [3,1,4,2]
nums_sorted = sorted(nums)
nums.sort()

#列表推导式
squares = [x**2 for x in range(10)]
print(squares)