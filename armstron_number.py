# def is_armstrong(num):
#     # Convert the number to a string to get the number of digits
#     num_str = str(num)
#     num_digits = len(num_str)
    
#     # Calculate the sum of each digit raised to the power of num_digits
#     sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    
#     # Check if the sum of powers is equal to the original number
#     return sum_of_powers == num

# # Example usage
# num = int(input("Enter a number: "))
# if is_armstrong(num):
#     print(f"{num} is an Armstrong number.")
# else:
#     print(f"{num} is not an Armstrong number.")

num = int(input("Enter Number: "))

num_str = str(num)
length_of_num = len(num_str)
total = 0

for i in num_str:
    total += int(i) ** int(length_of_num)
print(total)

if total == num:
    print("Armstron Number")
else:
    print("Not armstrongs")
