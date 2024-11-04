def triangle(n):
  value=1
  for i in range(n):
    for j in range (i+1):
      print(value,end=" ")
      value=value+1
    print()
triangle(5)
