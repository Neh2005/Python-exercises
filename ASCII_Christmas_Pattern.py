def tree(width,trunklength):
  for i in range (1,width+1,2):
    print (" " *(width-i//2) + "*"*(i))
   
  for j in range(1,trunklength+1,1):
    print(" "*(width-i//2)+" "*((width-i//2)//2)+"*"*trunklength )
  print("")
