"""
a = str(input("Enter alphabet to check whether it's a vowel or not: "))
v = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

if a in v:
    print("Alphabet is vowel")

else:
    print("Alphabet is consonant")
"""

def vow(char):
    all_vowels = "aeiouAEIOU"
    return char in all_vowels

print(vow(str(input("Enter character: "))))