# get input #
age = int(input("enter your age: "))

print("choose your citizenship")
print("1.kenyan")
print("2.other")
#choice input on citizenship #

citizenship = int(input("choose: "))
                  
isKenyan = (citizenship == 1)

if (age < 18):
    print("you are not eligible to vote")
elif(age >= 18 and isKenyan):
    print("youre eligible to vote")
elif(age < 1):
    print("invalid age entered")
else:
    print("youre not eligible")