import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    count = 0
    for n in range(numTrials):
        balls = ["r", "r", "r", "g", "g", "g"]
        i =0
        counter = []
        while i < 3:
            choice = random.choice(balls)
            balls.remove(choice)
            counter.append(choice)
            i += 1
        if counter == ["r","r","r"] or counter == ["g", "g", "g"]:
            count += 1
    return float(count)/numTrials
        
print noReplacementSimulation(5000)
            
        
        
        