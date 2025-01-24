# get input #
age = int(input("enter your age: "))
citizenship = input("Enter your citizenship: ")
if (citizenship == "Kenyan" or "ugandan" or "tanzanian"):
    if (age < 18):
        print("you are not eligible to vote")
    elif(age >= 18):
        print("youre eligible to vote")
    elif(age < 1):
        print("invalid age entered")
else:
    print("youre not eligible")