
# 使用“方法”修改字符串的大小写
first_name = "ada"
last_name = "love"


# 字符串的拼接
full_name = first_name+" " +last_name
print("hello,"+full_name.title()+"!")


#制表符和换行符的使用
print("\n\tzhang jie") 


#删除空白    
'''
开头空白（lstrip）  
尾空白（rstrip）
两端空白（strip）
'''
favorite_language = "     python     "
print(favorite_language)
favorite_language = favorite_language.strip()
print(favorite_language)


# 单引号和撇号一起用要慎重
# message = 'One of python's strengths is its diverse community.'
# 上面代码三个单引号，在解释器看来语法错误


# 函数str()的使用(可以把非字符串值23表示为字符2和3
age = 23
massage = "Happy " +str(age) +"rd birthday"
print(massage)

#python2中的整数

# 列表，用[  ]来表示，用逗号来分隔其中的元素
bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[-1])


#列表元素的修改，添加以及删除
#修改
names = ['小龙','臣谦','太水','张杰']
print(names)
names[2] = '汉灵'
print(names)
#列表末尾添加，列表中间添加
names.append('太水')
print(names)
names = ['小龙','臣谦','汉灵','张杰']
names.insert(0,'太水')
print(names)
#删除(del)(pop)(remove)
names = ['小龙','臣谦','汉灵','张杰','太水']
last_person = names.pop()
print(names)
print(last_person)
last_person = names.pop(2)
print(last_person)
names = ['小龙','臣谦','汉灵','张杰','太水']
names.remove('汉灵')
print(names)
motorcycles = ['honda','yamha','suzuki','ducati']
print(motorcycles)
too_expersive = 'ducati'
del motorcycles[-1]
print(motorcycles)
print("\nA " + too_expersive.title() + " is too expersive for me.")


#组织列表
#1：排序
# sort方法（永久性排序）
# sorted（临时排序）
# reverse（永久性反转列表元素）
#2：确定列表长度len（列表名称）
cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)
cars = ['bmw','audi','toyota','subaru']
print(sorted(cars))
print(cars)
cars.reverse()
print(cars)

''' 使用列表时一定注意避免索引错误，切记
列表索引存在差一的特征'''

# 操作列表
# for循环 (冒号和缩进切勿忘)
#使用for循环打印魔术师的名字
magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician)
#for循环后缩进的代码重复执行，不缩进的只执行一次
#避免缩进错误（一定不要忘记冒号）

#创建数值列表
# range()函数
for  number in range(0,5):
         print(number)
number = list(range(1,6))
print(number)
#打印1-10的平方，存到列表中
squares = [   ]
for number in range(1,11):
		squares.append(number**2)
print(squares)
#对数字列表进行简单的统计计算
number = range(0,4)
print(sum(number))
#列表解析
#使用列表的一部分（切片）类似于range（）
players = ['Tom','Jim','Marry','Zj']
print(players[0:2])       #差一特征
print(players[2:])      
print(players[:3])
#复制列表           [  :  ]
'''
my_food = ['pizza','carrot','apple']
friend_food = my_food[:]
上面这行代码不同于下一行，上面这行得到两个列表，
下面那行得到一个列表.
friend_food = my_food
'''

#元组
