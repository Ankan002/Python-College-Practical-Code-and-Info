lower_bound = int(input("Enter the lower bound: "))
upper_bound = int(input("Enter the upper bound: "))

print("The numbers that are multiple by 17 but not 5 between", upper_bound, "and", lower_bound, "are: ")

for i in range(lower_bound, upper_bound+1):
    if i % 17 == 0 and i % 5 != 0:
        print(i)
