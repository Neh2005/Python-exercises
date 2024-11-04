def table(num):
  print("x",end="\t")
  for i in range(num+1):
    print(str(i),end="\t")
  print()
  for j in range(num+1):
    print(str(j),end="\t")
    for k in range(num+1):
      print(str(j*k),end="\t")
    print()
table(12)
  

  
