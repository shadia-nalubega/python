# data types are categories of values we store in the memory
# 1 numeric e.g int, float,complex
# 2 string
# 3 sequence e.g list, tople and range
# 4 mapping e.g dictionary
# 5 boolean
# 6 set
'''
examples of numeric datatypes
'''
# integers (int) are whole numbers from 0-inf
my_num = 200
print(type(my_num))
# a float is any number with a decimal point e,g 0,0
my_num = 200.0
print(type(my_num))
# complex numbers comprise of an imaginary and real part denoted by a j/J
# sometimes we write them with the inbuilt complex  funtion
z = 2+4j
# z = complex(3 4)
# let my_num =200; or var my_num =200; if it's for c language, you would say init my_num = 200
# complex number
#string is a collection of characters and we identify them by putting them in quotes
name = "shadia"
my_num = "200"
# the process of creating a variable is called declaring
# the process of giving a name to a variable is called intialising/ assigning
# in python we declare and assign at the same time
'''
#sequence datatype
'''

# sequences are variables that can store more than one value
# a list 
# a list is identified by square brackets
# we use indices to identify values from both a list and a tuple
number = []
numbers2 = [5,10,15]
print(name)
print(type(numbers2))
print(numbers2)
print(numbers2[0])
print(numbers2[2])
print(numbers2[-1])
print(numbers2[1]+numbers2[-1])
my_stuff = ["ozzy",10,20,[40,60]]
print(my_stuff[3][0])
print(my_stuff[-1][-2])
animals = ["cats","dogs",[ "fish","shark",["rats","ducks"]]]
print(animals[2][2][0])
print(animals[-1][-1][-2])
print(animals[-1][-2])
print(animals[-1][-1][-1])
# list continued
my_stuff.append(1000)


print(my_stuff)
my_stuff.pop()
print(my_stuff)
#tuple is like a list but it is identified by a pair of oval brackets.they are immutable
numbers =(10,20,30)
print(numbers[1])
#mapping is the collection of values that are identified by their own keys or custom keys e.g 
car = {"name":["subaru" ,"noah" ],"model":"2027","color":"red"}
# print(car.keys())
# print(car.values())
# l am accessing all values in the dictionary
# car["name"] = "lamborgin"
# updated the name of the value but the same key
# print(car.values())
# print(car["name"])
# printing out just one value
# a set is a datatype that stores unordered  unique items 
# my_things = {10,20,20,10,20}
# print(my_things)
# my_things.add(50)
# print(my_things)
# my_things.discard(10)
# print(my_things)
# set1 = {1,2,3,4}
# set2 = {3,4,5,6}
#intersection
# print(set1 & set2)
#union
# print(set1|set2)
# difference
# print(set1-set2)
#symentric difference
# print(set1^set2)
# print(set2-set1)
print(car.values())



