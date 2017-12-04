#  练习2.3  字符串的拼接
full_name =  "eric"
print("hello "+full_name.title() +",""would you like to learn some Python today?")
# 练习2.4  改变字母大小写
name = "zhang  jie"
print(name.lower())
print(name.upper())
print(name.title())
# 练习2.5
# 张杰  输出一条名人名言  12/4
famous_person = "albert einstein"
print(famous_person.title()+' once said, "A person who never made a mistake never tried anything new."')
# 练习2.8
print(5+3)
print(3.0/2)
#练习3.1
names = ['小龙','臣谦','太水','张杰']
#练习3.4   和客人共进晚餐，列表元素的删除与添加
guest = ['小龙','臣谦','太水','汉灵']
print("I want to eat dinner with " + str(guest)+ "!")
busy = guest.pop()
print(guest)
print(busy+" is too busy,so can't come")
guest.append('石豪')
print(guest)
guest.insert(0,'建峰')
print(guest)
first = guest.pop(1)
print(first+" sorry,the chair isn't enough")
second = guest.pop(1)
print(second+" sorry,the chair isn't enough")
del guest[1]
del guest[1]
print(guest)
'''#练习4.4 一百万
number = [    ]
for num in range(0,1000001):
		number.append(num)
print(number)'''
#练习4.6 奇数
for  num in range(1,20,2):
	print(num)
#练习4.7          3的倍数存到列表
num =list(range(3,30,3))	
print(num)
#练习4.10 你的皮萨和我的皮萨（切片和for循环）
pizza_species = ['cheese pizza','sausage pizza','pepperoni pizza']
friend_pizza = pizza_species[:]
pizza_species.append('vegetable pizza')
friend_pizza.append('specialty pizza')
print("My facorite pizzas are:")
for  pizza in pizza_species:
	print(pizza)
print("My friend's facorite pizzas are:")
for pizza in friend_pizza:
	print(pizza)
