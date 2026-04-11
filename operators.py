# operaters are symbols or a character or a word that tells a computer what to do with an operan
# a value is called an operan in programming language
# an operan is what an operator acts upon
# operators are categorised into six i.e
# arithmetic(mathematical operators)
# assignment operators
# comparison operators
# logical operators
# special opertors
# bitwise operators
1
# arithmentic(mathematical)
# addition
num1, num2 = 10, 20
print(num1 + num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
#floor division the value is always an interger that is the rounded off interger. it is the number the computer always ignores the number before the zero e.g 0.8
print(num1//num2)
# this is a power or exponetial
print(num1**num2)
# percentage is a modulo which gives the remainder after division
# if we have 5%2 the answer is 1
print(num1%num2)
2
# assignment operators these are used to store a value in the memory
name = "shadia"
# additional assignment
num1 += 2 #num1 = num1 + 2
print(num1)
# subtraction assignment
num1-=2 # current value of num1 -2
print(num1)
num1 *= 2 # current value of num1 * 2
print(num1)
num1 /= 2
print(num1)
num1 //=2 # this  operator always gives the remainder
print(num1)

3
# comparision operator(equal to ==)
print(num1 == num2)
# comparision operator (not equal to)  
print(num1 != num2)# modulus sign
print(num1 > num2)
print(num1 < num2)
print(num1 >= num2)
print(num1 <= num2)

4
# logical operators
print((num1 < num2) and (num2 > num1)) # for both conditions to be true, we use and
print((num1 > num2) or (num2 > num1)) # either condition should be true to print true we use or
print( not True)
print( not False)

5
# special operators and we have identity and membership operators
# identity operators (is /is not)
print(num1 is not num2)
print(num1 is num2)
# membershipp ( in/ not in)
name = "shadia"
print("d" in name)
print("l" not in name)
print("a" not in name)


# trial exercise for operators
# even or odd checker
number = int(input("please enter your number"))
if number % 2 == 0:
    print(number)
else:
    print(not number)
print("try another number")

# simple calculator
def num(num1,num2): 
    num1 = input("please enter your first number")
    print(num1)
    num2 = input("please enter your second number")
    print(num2)
print(num1 + num2)


