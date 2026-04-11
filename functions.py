# a function is a  named,block of code and performs a specific task
def add():
    num1, num2 = 20, 10
    print(num1 + num2)
# at this moment, the function is not printed until it is called upon
add()
# this function prints even numbers
def even():
    for number in range(10):
        if number % 2 == 0:
            print(number)
even() 
# this function prints odd numbers           
def odd():
    for number in range(10):
        if number % 2 != 0:
            print(number)
odd() 
# functions are self contained and any variable out of it can't be accessed
num3 = 10
def my_stuff():
 num1, num2 = 30, 50
 print(num1 + num2 + num3)
my_stuff()
# variables in one functions are private in other functions 
def my_input():
    name = input("please input your name") # remember the variable name is on the same indent with the print.
    print(name)
my_input()  
def jane():
    for item in range(10):
        print(item)
jane()
# other names we have views in django , method,procedure.          