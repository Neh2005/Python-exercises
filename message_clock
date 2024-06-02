def solve(h, m):
   text=["one", "two", "three", "four", "five", "six", "seven", "eight","nine","ten", "eleven", "twelve", "thirteen", "fourteen", "quarter", "sixteen","seventeen", "eighteen", "nineteen", "twenty", "twenty-one","twenty-two", "twenty-three", "twenty-four", "twentyfive"," twenty-six", "twenty-seven", "twenty-eight", "twenty-nine", "half"]

# to handle even if entered minutes is greater than 60.
   extra_hours = m // 60
   remaining_minutes = m % 60
   h = (h + extra_hours) % 12
   if h == 0:
        h = 12
   m = remaining_minutes
   op=""
   if (m == 0):
      op = text[h - 1] + " o' clock"
   elif (m == 30):
      op = text[m - 1]+ " past " + text[h - 1]
   elif (m == 1):
      op = text[m - 1] + " minute past " + text[h - 1]
   elif (m == 15):
      op = text[m - 1]+ " past " + text[h - 1]
   elif (m < 30):
      op = text[m - 1] + " minutes past " + text[h - 1]
   elif (m==45):
      op = "quarter to " + text[h]
   else:
      op = text[59 - m] + " minutes to " + (text[h] if h < 12 else text[0])
   return op


if __name__=="__main__":
   h= int(input("Enter the hour"))
   m= int(input("Enter the minute"))
   print(solve(h,m))
