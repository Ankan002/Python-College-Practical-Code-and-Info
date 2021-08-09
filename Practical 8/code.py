def my_reverse(string):
    reverse_string = ""
    for i in range(len(string) - 1, -1, -1):
        reverse_string = reverse_string + string[i]

    return reverse_string


initial_string = str(input("Enter the string that you want to enter: "))
print("The reversed string is: ", my_reverse(initial_string))
