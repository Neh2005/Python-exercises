def count(number,order):
  n=number
  sum=0
  for i in range(n):
      n1=n%10
      sum=sum+n1**order
      n=n//10
  if sum==number:
    print("It is an Armstrong number")
  else:
    print("It is not an Armstrong number") 
  return sum
 
print(count(371,3))
