import random, pylab

# You are given this function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)

# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a list of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axes
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    #check to see if there is a title included or not
    if title != None:
        pylab.title(title)
        
    #set the labels
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    
    #create the histogram
    pylab.hist(values, bins = numBins)
    
    #disply the histogram
    pylab.show()
    
random.seed(100)                    
# Implement this -- Coding Part 2 of 2
def roll(die, numRolls):
    # set the longestRun to 1, this will store the longest run of a number
    longestRun = 1
    
    # set the count to 1, this counts the current run
    count = 1
    
    # this is previous die roll
    previousValue = 0
    
    #loop for the numRools
    for i in range(numRolls):
        
        #get the result of the die roll
        result = die.roll()

        #change the count depending on the comparison with the previousValue
        if result == previousValue:
            count += 1
        else:
            count = 1
        
        #update the longestRun    
        if longestRun < count:
            longestRun = count
         
        #update the previousValue   
        previousValue = result
    
    return longestRun

def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls, and the 95% confidence interval.
        Rounds the mean and confidence interval to 3 decimal places.
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """
    #stores longestRun for each trial in totals
    totals = []
    
    #calculate the longestRun for each trial and store it in totals
    for i in range(numTrials):
        result = roll(die, numRolls)
        totals.append(result)
    
    #print the histogram
    makeHistogram(totals, 10, "x-axis", "y-axis", "title")
    
    #calculate the mean
    mean, stdDev = getMeanAndStd(totals)

    return mean
        
 
# One test case
print getAverage(Die([1,2,3,4,5,6,6,6,7]), 500, 10000)