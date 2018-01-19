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

for i in range(1, 6,2):
    print i
    if i==5:
        break
else:
    print 'The for loop is over'