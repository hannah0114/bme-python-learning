#02_dict_tuple_set.py
#元组
point = (10.2, 20.5)

#字典
person = {"name":"张三","height":1.72,"weight":68}
print(person["name"])
for k,v in person.items():
    print(k, v)

#集合
s1 = {1,2,2,3,3,3}
s2 = {2,3,4}
print(s1 & s2) #交集
print(s1 | s2) #并集
print(s1 - s2) #差集