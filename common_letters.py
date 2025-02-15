#Find Common Letters

word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

w1 = set(word1) #removes duplicates if any
w2 = set(word2)

common_letters = set()

for letter in word1: #loop through each letter
    if letter in w2: #if in word2
        common_letters.add(letter) #add them to set

sorted_common_letters = sorted(common_letters, key=lambda x: word1.index(x)) #sort them as they appear

if common_letters:
    print(f"Common letters are: {sorted_common_letters}") #print common letters
else:
    print(f"No common letters found.")

