#!/usr/bin/python
# coding:utf-8
# Filename: test1.py

# print 'hello '
# i = 5
# print i
# i = i + 1
# print i

# s = '''This is a multi-line string.
# This is the second line.'''
# print s
# i = 5
# print 'Value is', i # Error! Notice a single space at the start of the line
# print 'I repeat, the value is', i

# number = 23
# guess = int(raw_input('Enter an integer : '))

# if guess == number:
#     print 'Congratulations, you guessed it.' # New block starts here
#     print "(but you do not win any prizes!)" # New block ends here
# elif guess < number:
#     print 'No, it is a little higher than that' # Another block
#     # You can do whatever you want in a block ...
# else:
#     print 'No, it is a little lower than that' 
#     # you must have guess > number to reach here

# print 'Done'
# # This last statement is always executed, after the if statement is executed
# number = 23
# running = True

# while running:
#     guess = int(raw_input('Enter an integer : '))

#     if guess == number:
#         print 'Congratulations, you guessed it.' 
#         running = False # this causes the while loop to stop
#     elif guess < number:
#         print 'No, it is a little higher than that' 
#     else:
#         print 'No, it is a little lower than that' 
# else:
#     print 'The while loop is over.' 
#     # Do anything else you want to do here

# print 'Done'

# for i in range(1, 6,2):
#     print i
#     if i==5:
#         break
# else:
#     print 'The for loop is over'

# def func():
#     global x

#     print 'x is', x
#     x = 2
#     print 'Changed local x to', x

# x = 50
# func()
# print 'Value of x is', x
# def func(a=1, b=5, c=10):
#     print 'a is', a, 'and b is', b, 'and c is', c

# func(3, 7)
# func(25, c=24)
# func(c=50, a=100)
# func()


# def someFunction():
#     pass

# def printMax(x, y):
#     '''Prints the maximum of two numbers.

#     The two values must be integers.'''
#     x = int(x) # convert to integers, if possible
#     y = int(y)
#     if x > y:
#         print x, 'is maximum'
#     else:
#         print y, 'is maximum'

# printMax(3, 5)
# print printMax.__doc__


# help(printMax)

# import sys
# print dir(sys)
# print 'The command line arguments are:'
# for i in sys.argv:
#     print i

# print '\n\nThe PYTHONPATH is', sys.path, '\n'
# if __name__ == '__main__':
#     print 'This program is being run by itself'
# else:
#     print 'I am being imported from another module'

# print __name__

# print dir()
# a=5
# print dir()
# del a
# print dir()
# shoplist = ['apple', 'mango', 'carrot', 'banana']

# print 'I have', len(shoplist),'items to purchase.'

# print 'These items are:', # Notice the comma at end of the line
# for item in shoplist:
#     print item,

# print '\nI also have to buy rice.'
# shoplist.append('rice')
# print 'My shopping list is now', shoplist

# print 'I will sort my list now'
# shoplist.sort()
# print 'Sorted shopping list is', shoplist

# print 'The first item I will buy is', shoplist[0]
# olditem = shoplist[0]
# del shoplist[0]
# print 'I bought the', olditem
# print 'My shopping list is now', shoplist


# zoo = ('wolf', 'elephant', 'penguin')
# print 'Number of animals in the zoo is', len(zoo)

# new_zoo = ('monkey', 'dolphin', zoo)
# print 'Number of animals in the new zoo is', len(new_zoo)
# print 'All animals in new zoo are', new_zoo
# print 'Animals brought from old zoo are', new_zoo[2]
# print 'Last animal brought from old zoo is', new_zoo[2][2]



# ag


# print 'Simple Assignment'
# shoplist = ['apple', 'mango', 'carrot', 'banana']
# mylist = shoplist # mylist is just another name pointing to the same object!引用

# del shoplist[0]

# print 'shoplist is', shoplist
# print 'mylist is', mylist
# # notice that both shoplist and mylist both print the same list without
# # the 'apple' confirming that they point to the same object

# print 'Copy by making a full slice'
# mylist = shoplist[:] # make a copy by doing a full slice拷贝
# del mylist[0] # remove first item

# print 'shoplist is', shoplist
# print 'mylist is', mylist
# # notice that now the two lists are different



name = 'Swaroop' # This is a string object 

if name.startswith('Swa'):
    print 'Yes, the string starts with "Swa"'

if 'a' in name:
    print 'Yes, it contains the string "a"'

if name.find('war') != -1:
    print 'Yes, it contains the string "war"'

delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print delimiter.join(mylist)