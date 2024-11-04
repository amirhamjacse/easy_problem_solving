# def is_prime(num):

#     if num < 2:
#         return False

#     for i in range(2, num):
#         if num % i == 0:
#             return False

#     return True

# # Example usage
# num = int(input("Enter a number: "))
# if is_prime(num):
#     print(f"{num} is a prime number.")
# else:
#     print(f"{num} is not a prime number.")5


num = int(input("Input Number: "))
if num <2:
    print("It is not prime number")
else:
    for i in range(2, num):
        if num % i ==0:
            print("it is not prime number")
            break
    else:
        print("It is Prime")