#isalnum
# contains either numeric or alphabet
string1 = "M234onica"
print(string1.isalnum()) # True 
# contains whitespace
string2 = "M3onica Gell22er"
print(string2.isalnum()) # False
# contains non-alphanumeric character 
string3 = "@Monica!"
print(string3.isalnum()) # False 

#isalpha
name = "Monica"
print(name.isalpha())
# contains whitespace
name = "Monica Geller"
print(name.isalpha())
# contains number
name = "Mo3nicaGell22er"
print(name.isalpha())

#endswith
message = 'Python is fun'
# check if the message ends with fun
print(message.endswith('fun'))
# Output: True

#capitalize
sentence = "i love PYTHON"
# converts first character to uppercase and others to lowercase
capitalized_string = sentence.capitalize()
print(capitalized_string)
# Output: I love python

#center
sentence = "Python is awesome"
# returns the centered padded string of length 24 
new_string = sentence.center(24, '*')
print(new_string)
# Output: ***Python is awesome****

#casefold
text = "pYtHon"
# convert all characters to lowercase
lowercased_string = text.casefold()
print(lowercased_string)
# Output: python

#count
message = 'python is popular programming language'
# number of occurrence of 'p'
print('Number of occurrence of p:', message.count('p'))
# Output: Number of occurrence of p: 4

#format
# default arguments
print("Hello {}, your balance is {}.".format("Adam", 230.2346))
# positional arguments
print("Hello {0}, your balance is {1}.".format("Adam", 230.2346))
# keyword arguments
print("Hello {name}, your balance is {blc}.".format(name="Adam", blc=230.2346))
# mixed arguments
print("Hello {0}, your balance is {blc}.".format("Adam", blc=230.2346))

#Output:
#Hello Adam, your balance is 230.2346.
#Hello Adam, your balance is 230.2346.
#Hello Adam, your balance is 230.2346.
#Hello Adam, your balance is 230.2346.

#index
text = 'Python is fun'
# find the index of is
result = text.index('is')
print(result)
# Output: 7

#isdecimal
s = "28212"
print(s.isdecimal()) #True
# contains alphabets
s = "32ladk3"
print(s.isdecimal())#False
# contains alphabets and spaces
s = "Mo3 nicaG el l22er"
print(s.isdecimal())#False

#isdigit
str1 = '342'
print(str1.isdigit())
str2 = 'python'
print(str2.isdigit())
# Output: True
#         False

#isidentifier
tr = 'root33'
if str.isidentifier() == True:
  print(str, 'is a valid identifier.')
else:
  print(str, 'is not a valid identifier.')
str = '33root'
if str.isidentifier() == True:
  print(str, 'is a valid identifier.')
else:
  print(str, 'is not a valid identifier.')
str = 'root 33'
if str.isidentifier() == True:
  print(str, 'is a valid identifier.')
else:
  print(str, 'is not a valid identifier.')
#root33 is a valid identifier.
#33root is not a valid identifier.
#root 33 is not a valid identifier.

#isnumeric
pin = "523"
# checks if every character of pin is numeric 
print(pin.isnumeric())
# Output: True

#isprintable
text1 = 'python programming'

# checks if text1 is printable 
result1 = text1.isprintable()
print(result1)
text2 = 'python programming\n'
# checks if text2 is printable 
result2 = text2.isprintable() 
print(result2)
empty_string = ' '
# returns True with an empty string 
print(empty_string.isprintable())
#True
#False
#True

#isspace
s = '\t  \n'
if s.isspace() == True:
  print('All whitespace characters')
else:
  print('Contains non-whitespace characters')
s = '2+2 = 4'
if s.isspace() == True:
  print('All whitespace characters')
else:
  print('Contains non-whitespace characters.')

#istitle
s = 'Python Is Good.'
print(s.istitle())
s = 'Python is good'
print(s.istitle())
s = 'This Is @ Symbol.'
print(s.istitle())
s = '99 Is A Number'
print(s.istitle())
s = 'PYTHON'
print(s.istitle())
#True
False
True
True
False

#join
text = ['Python', 'is', 'a', 'fun', 'programming', 'language']
# join elements of text with space
print(' '.join(text))
# Output: Python is a fun programming language

#swapcase
name = "JoHn CeNa"
# converts lowercase to uppercase and vice versa
print(name.swapcase())
# Output: jOhN cEnA

#strip() Parameters
random_string = '   this is good '
# first and end whitepsace are removed
print(random_string.strip())

#replace
text = 'bat ball'
# replace 'ba' with 'ro'
replaced_text = text.replace('ba', 'ro')
print(replaced_text)
# Output: rot roll

#split
text = 'Python is fun'
# split the text from space
print(text.split())
# Output: ['Python', 'is', 'fun']

#rsplit
grocery = 'Milk, Chicken, Bread, Butter'
# maxsplit: 2
print(grocery.rsplit(', ', 2))
# maxsplit: 1
print(grocery.rsplit(', ', 1))
# maxsplit: 5
print(grocery.rsplit(', ', 5))
# maxsplit: 0
print(grocery.rsplit(', ', 0))
#Output
#['Milk, Chicken', 'Bread', 'Butter']
#['Milk, Chicken, Bread', 'Butter']
#['Milk', 'Chicken', 'Bread', 'Butter']
#['Milk, Chicken, Bread, Butter']

#title
title() method returns a title cased version of the string. 
Meaning, the first character of each word is capitalized 
(if the first character is a letter).

#startswith
message = 'Python is fun'
# check if the message starts with Python
print(message.startswith('Python'))
# Output: True
