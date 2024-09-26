# Writing a function to check if the two entered strings are anagrams or not

def check_anagrams(string1, string2):
    return sorted(string1.lower()) == sorted(string2.lower())

string1 = input("Enter string1 : ")
string2 = input("Enter string2 : ")

print(check_anagrams(string1, string2))