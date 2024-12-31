# Check if a string is a palindrome
def is_palindrome(string):
    string = string.lower().replace(" ", "")
    return string == string[::-1]


word = input("Enter a word or phrase: ")
if is_palindrome(word):
    print(f"'{word}' is a palindrome!")
else:
    print(f"'{word}' is not a palindrome.")
