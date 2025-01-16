amount_input = input("Enter the total amount: ")
if (amount_input.isdigit()):
    amount = int(amount_input)
    if isinstance(amount, int):
        if (amount>5000):
            discount = 0.1*amount
            print("the discount is: ",discount)
            print("total discounted amount is: ", amount - discount)
        elif (amount >1000):
            discount = 0.05*amount
            print("the discount is: ",discount)
            print("the total discounted amount is: ", amount - discount)
        elif (amount <1):
            print("invalid amount")
        else:
            print("your amount is ", amount ,"without discount")
else:
    print("invalid ")
