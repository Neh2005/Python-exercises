def binaryToInt(binaryList):
    ''' Convert binary to int.  Input list of 4 bit binary numbers.  Output list of int numbers divisible by 3'''
    intList=[]
    list=[]
# initialize a binary string
    for i in binaryList:
        value=int(str(i), 2)
        if value%3==0:
            intList.append(str(i))
            list.append(str(value))
    print(",".join(intList))
    print(",".join(list)) 
    
print(binaryToInt([1011,1110,1111,11]))
