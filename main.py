# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


from wsgiref.handlers import SimpleHandler


def find_anagram(word, anagram):
    # [assignment] Add your code here
    length_word = len(word)
    length_anagram = len(anagram)

    # If the lenght of both strings are not the same, then they are not anagram
    if length_word != length_anagram:
        return False
    word = sorted(word)
    anagram = sorted(anagram)
    for i in range (0, length_word):
        if word[i] != anagram[i]:
            return False

    return True
word = "lies"
anagram = "sile"
if find_anagram(word, anagram):
    print(
    "The two strings are anagram of each other")
else:
    print(
    "The two strings are not anagram of each other")

