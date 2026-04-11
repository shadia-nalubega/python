# how to make functions share values(communicate)
def salary():
    gross = 2000000
    return gross  # make this value accessible
    staff = 300000
# exposing the salary to the tax
def tax():
    return salary()*0.3
print(tax()) 
def net():
    print(salary()-tax()) 
net() 
# Assignment 
# Write down steps each with code examples on how to create functions to calculate someone's net pay after tax
# Ozzy receives 10,000,000 and subjected to a tax of 18%, calculate his net pay
# declaring a function to use
def pay(): 
    gross = 10000000
# exposing the gross to other functions, we will use the return condition for the pay function
    return gross
# The tax function
def tax1():
# using the pay in the tax function
    return pay()*0.18  #calculating the tax. we will get the value of the tax Ozzy is subjected to
# we will now calculate Ozzy's netpay
# we will first define a function
def net1():
    print(pay()-tax1())
net1() 

 