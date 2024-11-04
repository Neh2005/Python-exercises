def language(langu):
   str1="English"
   str2="French"
   str3="Mandarin"
   if(langu==str1.casefold()): #casefold() is used to make string case insensitive
     print("Hello")
   elif(langu==str2.casefold()):
     print("Bonjour")
   elif(langu==str3.casefold()):
     print("Ni Hao")
   else:
     print("Sorry,but I don't speak that.")
   print("Welcome to Coventry")
if __name__=="__main__":
   lan= input("Enter your language") #prompt the user to enter their language and check whether it is one of the given three languages 
   language(lan)
