# Registration for voting
print(" Welcome to voting Elligibility")
print("Let's see if you are eligible to vote")
age = int(input("Please enter your age: "))
citizen = input("Are you a legal citizen of the US? (y/n): ")
reg = input("Are you registered to vote? (y/n): ")
status = input("Are you currently incarerated? (y/n: ")
eligible = False 

if age >= 18 and citizen == "y" and reg == "y" and status == "n":
    eligible = True

    if eligible:
        print("You are eligible to vote!")
else:
    print("Sorry, you are not eligible to vote.")
