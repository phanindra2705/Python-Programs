# Count words in a text file
def word_count(filename):
    try:
        with open(filename, "r") as file:
            text = file.read()
            words = text.split()
            print(f"The file '{filename}' has {len(words)} words.")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

filename = input("Enter the filename: ")
word_count(filename)
