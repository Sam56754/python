# program to perform operations on a lis of input from user

names = input("Enter the names: ").split()
sorted_names = sorted(names) # sort the names alphabetically
print("names list: ")
for name in sorted_names:
    print(name) 
print("The total number of names is: ", len(sorted_names)) #displays the list size