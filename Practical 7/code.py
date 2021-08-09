def largest(list_of_numbers):
    largest_num = list_of_numbers[0]
    for i in range(1, len(list_of_numbers)):
        if list_of_numbers[i] > largest_num:
            largest_num = list_of_numbers[i]
    return largest_num


size_of_list = int(input("Enter the number of elements that you want to enter: "))
list_numbers = []
print("Enter the numbers: ")
for j in range(size_of_list):
    list_numbers.append(int(input()))

print("The largest number from the numbers entered is: ", largest(list_numbers))
