# Get input
age = int(input("Enter your age: "))
citizenship = input("Enter your citizenship: ").lower()  # Convert input to lowercase

# Compare with available string values 
if citizenship in ["kenyan", "ugandan", "tanzanian"]:
    if age < 1:
        print("Invalid age entered")
    elif age < 18:
        print("You are not eligible to vote")
    else:
        print("You are eligible to vote")
else:
    print("You are not eligible")
