import pylab

# You may have to change this path
WORDLIST_FILENAME = "/Users/andrewmarmion/Google Drive/Python/6.00.2x/Lecture 4/L4P5/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of uppercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def plotVowelProportionHistogram(wordList, numBins=15):
    """
    Plots a histogram of the proportion of vowels in each word in wordList
    using the specified number of bins in numBins
    """
    vowelProportions = tallyVowels(wordList) 

    pylab.hist(vowelProportions, bins = numBins)
    xmin, xmax = pylab.xlim()
    ymin, ymax = pylab.ylim()
    print 'x-range =', xmin, '-', xmax
    print 'y-range =', ymin, '-', ymax
    pylab.figure
    pylab.show()


    
def tallyVowels(wordList):
    vowelCounts = []
    for word in wordList:
        vowelCount = 0.0
        for character in word:
            if character in ['a', 'e', 'i', 'o', 'u']:
                vowelCount += 1

        proportion = vowelCount / len(word)
        vowelCounts.append(proportion)

    return vowelCounts
    

if __name__ == '__main__':
    wordList = loadWords()
    plotVowelProportionHistogram(wordList)
