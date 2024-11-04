# def is_palindrome(num):
#     # Convert the number to a string
#     num_str = str(num)
    
#     # Check if the string is equal to its reverse
#     return num_str == num_str[::-1]

# # Example usage
# num = int(input("Enter a number: "))
# if is_palindrome(num):
#     print(f"{num} is a palindrome.")
# else:
#     print(f"{num} is not a palindrome.")


num = int(input("Enter number"))
num_str = str(num)
if num_str == num_str[::-1]:
    print("Palindrom")
else:
    print("Not palindrom")