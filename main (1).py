#Write a program that determines whether a year entered by the user is a leap year for not using if- elif-else statements.

def checkleepyear(year):
  if(year%4==0):
    return True
  else:
    return False

year=int(input("Enter a year:"))
if checkleepyear(year):
  print(year,"is a leep year")
else:
  print(year,"is not a leep year")