import random
def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    
    Deterministic functions: 
    These models perform the same way for a given set of initial conditions, 
    and it is possible to predict precisely what will happen. 
    Therefore only one result will be generated everytime the function is run
    '''
    return 10
    
for i in range(0,1000):
    if deterministicNumber() % 2 != 0:
        print "not even"
        
def stochasticNumber():
    '''
    Stochastically generates and returns a uniformly distributed even number between 9 and 21
    '''
    # Your code here
    return random.randrange(10, 21, 2)
    
print stochasticNumber()  