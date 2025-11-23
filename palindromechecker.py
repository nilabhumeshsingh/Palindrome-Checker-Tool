word = input("Palindrome Checker Tool")
for i in range (0, len(word)):
    if word[i] == word[-i -1]:
            i += 1
    else:
        print(f"{word} is not a Palindrome Checker Tool")
        break
if i == len(word):
     print(f"{word} is a Palindrome Checker Tool")
