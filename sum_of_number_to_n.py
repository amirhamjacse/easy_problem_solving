#Write a program that asks the user for a number n and prints the sum of the numbers 1 to n

number = int(input("Enter a number: "))

sum = 0 

for i in range(1, number+1):
    sum += i
    # print(i)

print("Sum of the number series: ", sum)
