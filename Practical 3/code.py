#taking input for the sentence with 5 words
sentence = str(input("Enter a sentence with at least 5 words in it: "))

#printing the initial sentence entered by the user
print(sentence)

#converting sentence into list of words
list_of_words = sentence.split(" ")

#sorting and reversing the list alphabetically
list_of_words.sort()
list_of_words.reverse()

#printing out the the sorted & reversed list
print("The sorted and reversed List: ")
print(list_of_words)
