# myScore = int(input("Your score: "))
# if myScore > 100000:
#   print("Winner!")
# else:
#   print("Try again 😭")

# myPi = float(input("What is Pi to 3dp? "))
# if myPi == 3.142 :
#   print("Exactly!")
# else:
#   print("Try again 😭")

# score = int(input("What was your score on the test?"))
# if score >= 80:
#   print("Not too shabby")
# elif score >= 70:
#   print("Acceptable.")
# else:
#   print("Dude, you need to study more!")

print("Generation Identifier")

born_date = int(input("Which year were you born? "))

if born_date <= 1946:
    print("You are a Traditionalist")
elif born_date >= 1947 and born_date <= 1964:
    print("You are a Baby Boomer")
elif born_date >= 1965 and born_date <= 1981:
    print("You are a Generation X")
elif born_date >= 1982 and born_date <= 1995:
    print("You are a Millenial")
elif born_date >= 1996:
    print("You are a Generation Z")
