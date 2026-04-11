# loops are  a mechanism of how to instruct a computer to repeatedly /iterate perform something until a certain condition is met and it is false
# for loop
for number in range(10):
    print(number)
mylist = {10, 20,30,40,50,60}
# added these items to the previous numbers
for item in mylist:
    print(item)
# we print only numbers with a remainder 0 after dividing with 2    
for number in range(20):
    if number % 2 == 0:
     print(number)
# we print only numbers without remainder 0 after dividing with 2    
for number in range(20):
    if number % 2 != 0:
     print(number)
# loops are memory monster(consumes alot of memory)




