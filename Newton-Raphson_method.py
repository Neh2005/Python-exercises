def mySqrt(x):
  if x>=0:
    y=(x+1)/2

    while True:
      if y**2 < x+0.001 and y**2 > x-0.001:
        return y 
      y=(y+x/y)/2
      
print(mySqrt(9))
