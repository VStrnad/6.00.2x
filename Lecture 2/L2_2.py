import random
def genEven():
    '''
    Returns a random even number x, where 0 <= x < 100
    
    random.randrange(a, b, c)
    
    c is the step between each random number. 
    By setting it to 2 it makes the output even numbers 
    
    http://docs.python.org/2/library/random.html

    '''
    return random.randrange(0, 100, 2)
    

for i in range(0,1000):
    if genEven() % 2 != 0:
        print "not even"
