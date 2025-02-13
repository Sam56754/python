#electricity bill calculator

#input customer details
customerID = input("Enter custromer id:")
customerName = input("Enter customer name: ")
units_consumed = float(input("Enter units consumed: "))

#calculate the payment per units
if units_consumed <= 199:
    charges = units_consumed * 1.20
elif units_consumed >=200 and units_consumed < 400:
    charges = units_conumed * 1.50
elif units_consumed >= 400 and units_consumed < 600:
    charges = units_consumed * 1.80
elif units_consumed >= 600:
    charges = units_consumed * 2.00

#function to print the customer details
def details():
    print("\nCustomer ID",customerID)
    print("Name: ",customerName)
    print("units consumed : ", units_consumed)

#check whether the customer has to pay extra surcharge
if charges > 400:
    surcharge = charges + (0.15 * charges)
    details()
    print("your charges per unit are: ", charges/units_consumed)
    print("your total bill is: Kshs", surcharge)
elif charges < 99:
    details()
    print("your charges per unit are: ", charges/units_consumed)
    print("Your total bill is: Kshs 100.0")
else:
    details()
    print("your charges per unit are: ", charges/units_consumed)
    print("your bill is : Kshs ",charges)
