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



age = 22
name = 'Swaroop'

print '%s is %d years old' % (name, age)
print 'Why is %s playing with that python?' % name


# 'ab' is short for 'a'ddress'b'ook

ab = {       'Swaroop'   : 'swaroopch@byteofpython.info',
             'Larry'     : 'larry@wall.org',
             'Matsumoto' : 'matz@ruby-lang.org',
             'Spammer'   : 'spammer@hotmail.com'
     }

print "Swaroop's address is %s" % ab['Swaroop']

# Adding a key/value pair
ab['Guido'] = 'guido@python.org'

# Deleting a key/value pair
del ab['Spammer']

print '\nThere are %d contacts in the address-book\n' % len(ab)
for name, address in ab.items():
    print 'Contact %s at %s' % (name, address)

if 'Guido' in ab: # OR ab.has_key('Guido')
    print "\nGuido's address is %s" % ab['Guido']


shoplist = ['apple', 'mango', 'carrot', 'banana']

# Indexing or 'Subscription' operation
print 'Item 0 is', shoplist[0]
print 'Item 1 is', shoplist[1]
print 'Item 2 is', shoplist[2]
print 'Item 3 is', shoplist[3]
print 'Item -1 is', shoplist[-1]
print 'Item -2 is', shoplist[-2]

# Slicing on a list
print 'Item 1 to 3 is', shoplist[1:3]
print 'Item 2 to end is', shoplist[2:]
print 'Item 1 to -1 is', shoplist[1:-1]
print 'Item start to end is', shoplist[:]

# Slicing on a string
name = 'swaroop'
print 'characters 1 to 3 is', name[1:3]
print 'characters 2 to end is', name[2:]
print 'characters 1 to -1 is', name[1:-1]
print 'characters start to end is', name[:]