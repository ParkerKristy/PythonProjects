#1 Importance of types
#make sure you are using 'str' and 'int' correctly

a = input("Enter some input ") #5
print(type(a))  #<class 'str'>
#print(a +10)
# 10 + a ->Type error: can only concatenate str (not "int") to str
print(a * 10) # 5555555555


b = int(a)
print(type(b))
print(b + 10)
#10 + b = 15

print(b * 10) #50

#2 Importance of types

#int - whole number
#float - decimal number

a= float("10")
print(a) #10.0

int("10")  #10
#you can convert int or float to 'str'

#3 List indexing

mylist = ['a', 'b', 'c']
z = mylist[1]
print(z) #b

print(mylist.index('b')) #gives you index number

#python console dir(list) - gives you list methods

#to change  values in the list
mylist.__setitem__(1, 'd')
print(mylist)
#also can be done by
mylist[1] = 'e'

#to get item from the list
mylist.__getitem__(2) #'c'
#also can be done by
mylist[2]