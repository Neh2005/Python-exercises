#sort the list in the order of how close a number is to 50
def myfunc(n):
  return abs(n - 50)
thislist = [ 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#insert method
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
 #['apple', 'banana', 'blackcurrant', 'watermelon'] (answer)

#concatenation of two lists
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
#['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya'] (answer)

#deletion of elements from the lists
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
#['apple', 'cherry']

#pop() method
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
#['apple', 'banana']

#deletion of the elements
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
#['banana', 'cherry']

#deletion the entire list
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
#[]

#print all the elements in the list
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
#apple
#banana
#cherry

#sort() method type 1
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
#['banana', 'kiwi', 'mango', 'orange', 'pineapple']

#reverse the list type 1 with only small letter strings
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
#['pineapple', 'orange', 'mango', 'kiwi', 'banana']

#sort() method type 2 with Capital letter strings
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
#['Kiwi', 'Orange', 'banana', 'cherry']

#soring lists from smaller case to Bigger case strings
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
#['banana', 'cherry', 'Kiwi', 'Orange']

#reversing lists type 2 with Capital letter strings
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist) 
#['cherry', 'Kiwi', 'Orange', 'banana']

#copy the entire list
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
#['apple', 'banana', 'cherry']

#slice method
txt = "Hello World"[::-1]
print(txt)
