# python program to calculate the discount offered on purchase amount (>5000 gets 10% disc , >1000 gets 5%disc and the rest no discount)

amount_input = input("Enter the total amount: ")
if (amount_input.isdigit()): #check if input is numbers #
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
        elif (amount <1): # edge case for negative input #
            print("invalid amount")
        else:
            print("your amount is ", amount ,"without discount")
else:
    print("invalid character identified")