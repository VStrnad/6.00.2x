def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    lengths = []
    tot = 0
    if len(L) == 0:
        return NaN
        
    for x in L:
        lengths.append(len(x))
    mean = sum(lengths)/float(len(lengths))

    for x in lengths:
        tot += (x-mean)**2
    return (tot/len(lengths))**0.5
        
        