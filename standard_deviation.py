from statistics import stdev
def myStdDev(inList):
    c=stdev(inList)
    return round(c)
myStdDev(inList=[11,22,33,44,55,66,77,88,99])
