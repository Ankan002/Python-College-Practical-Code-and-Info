def is_palindrome(sentence):
    pure_string = ""
    for i in sentence:
        if i.isalpha() or i.isdigit():
            pure_string = pure_string + i
    if len(pure_string) == 0:
        return True
    pure_string = pure_string.lower()
    i = 0
    j = len(pure_string)-1
    palindrome = False
    while i <= j:
        if pure_string[i] == pure_string[j]:
            palindrome = True
        else:
            palindrome = False
            break
        i = i + 1
        j = j - 1
    return palindrome


string = str(input("Enter the string: "))
if is_palindrome(string):
    print("The given string is palindrome")
else:
    print("The given string is not palindrome")
