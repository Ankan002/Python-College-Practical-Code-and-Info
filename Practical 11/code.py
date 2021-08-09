string = str(input("Enter the string for which you want to find the ASCII value: "))
new_ascii = ""
for c in string:
    new_ascii = new_ascii + str(ord(c))
print("ASCII value of", string, "is:", new_ascii)
