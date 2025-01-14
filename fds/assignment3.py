
# Longest Word
string = input("Enter the string to find longest word: ")

string_list = string.split()
longest = 0
index = 0
for i in range(len(string_list)):
    if len(string_list[i]) > longest:
        longest = len(string_list[i])  
        index = i

print(f"Longest word in the string is: {string_list[index]}")

# Number of occurence of character

print("Enter the character you want to count the occurence of: ")
char = input()[0]
count = 0
for i in string:
    if char == i:
        count += 1

print(f"Occurence of char {char} in string is: {count} times")

# Palindrome Check

string = input("Enter the string: (for palindrome check) ")

if string[::-1] == string:
    print("String is a palindrome")
else:
    print("String is not a palindrome")

# Subtring finding

string = input("Enter a sentence: ")

print("Enter the substring you want to search for: ")
sub_string = input()

index = string.find(sub_string)
if index==-1:
    print("No substring found")
else:
    print(f"Index of substring in string is at: {string.find(sub_string)}")

# Number of occurence of word finding

words = []
occurence = []

word_counts = {}  # Create an empty dictionary to store word counts
  # Split the text into words (case-insensitive)
for word in string.lower().split():
    # Remove non-alphanumeric characters
    if word:  
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
print(word_counts)
