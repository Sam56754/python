# A python program to asses overdue dates on library books and calculate the fine rates

bookID = input("Enter the book ID: ")
returnDate = int(input("Enter the return date: "))
dueDate = int(input("Enter the due date: "))

days = returnDate - dueDate  # Calculate overdue days

# Function to calculate fine
def fine(days):
    if days <= 0:
        return 0  # No fine if the book is returned on time
    elif days <= 7:
        return days * 20  # First 7 days: 20 Ksh per day
    elif 7 < days <= 14:
        return (7 * 20) + ((days - 7) * 50)  # Next 7 days: 50 Ksh per day
    else:
        return (7 * 20) + (7 * 50) + ((days - 14) * 100)  # After 14 days: 100 Ksh per day

#fine
ksh = fine(days)

#fine rate 
fine_rate = ksh / days

print("\nThe book ID:", bookID)
print("Your overdue days:", days)
print("Your fine is:", ksh, "Ksh")
print(f"Your fine rate is: {fine_rate:.2f} Ksh/day")
