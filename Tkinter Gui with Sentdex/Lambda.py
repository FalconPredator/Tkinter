'''


# assign lambda function to variable
add = lambda x,y:x+y   
print(add(1, 2))


# assign lambda function to function
import time
time.sleep = lambda x: None # mute time.sleep
time.sleep(3)
print ('y')


print(filter(lambda x: x % 3 == 0, [1, 2, 3]))


def example(x, y):
	return (lambda x, y: x * y)

print(example(2, 9))
'''
a=1
lambda a: print(2)