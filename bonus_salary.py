#bonus according to time period

#input details
salary = int(input("Enter your salary: "))
years = int(input("Enter your years of service: "))

#check the years to allocate the bonus
if years > 10 and years <100:
    bonus = 0.1 * salary
elif years >=6 and years <=10:
    bonus = 0.08 * salary
elif years < 6 and years > 0:
    bonus = 0.05 * salary
else:
    print("invalid number")
    
print("\nYour bonus is KSH ",bonus)
print("your net bonus salary is: ", bonus + salary)