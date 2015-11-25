# generate all combinations of N items
def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in xrange(2**N):
        combo = []
        for j in xrange(N):
            # test bit jth of integer i
            if (i / (2**j)) % 2 == 1: # instead of  (i >> j) % 2 == 1
                combo.append(items[j])
        yield combo
        
        
def yieldAllCombos(items):
    """
      Generates all combinations of N items into two bags, whereby each 
      item is in one or zero bags.

      Yields a tuple, (bag1, bag2), where each bag is represented as 
      a list of which item(s) are in each bag.
      
      There are three possible outcomes
      bag1
      bag2 
      discarded
    """
    N = len(items)
    for i in xrange(3**N):
        bag1, bag2, discarded = [], [], []
        for j in xrange(N):
            if(i / (3**j)) % 3 == 0:
                bag1.append(items[j])
            elif (i / (3**j)) % 3 == 1:
                bag2.append(items[j])
            elif (i / (3**j)) % 3 == 2:
                discarded.append(items[j])
    
        yield (bag1, bag2)
        
        
items = ["a","b","c","d"]
foo = yieldAllCombos(items)
i = 0
while i < 3**(len(items)):
    print i, foo.next()
    i+=1


        