# def are_anagrams(str1, str2):
#     # Remove spaces and make both strings lowercase
#     str1 = str1.replace(" ", "").lower()
#     # print(sorted(str1), 'first')
#     str2 = str2.replace(" ", "").lower()
#     # print(sorted(str2), 'second')
    
#     # Compare the sorted characters of both strings
#     return sorted(str1) == sorted(str2)

# # Example usage
# str1 = "listen"
# str2 = "silent"
# print(are_anagrams(str1, str2))  # Output: True

#without function

str1 = "listen"
str2 = "SiLent"

str1convt = str1.replace(" ", "").lower()
str2convt = str2.replace(" ", "").lower()

if sorted(str1convt) == sorted(str2convt):
    print("Annagram")
else:
    print("Not Anagram")

