#Write a program that asks the user for a number n and prints the sum of the numbers 1 to n

number = int(input("Enter a number: "))

sum = 0 

for i in range(1, number+1):
    sum += i
    # print(i)

print("Sum of the number series: ", sum)


#Modify the previous program such that only multiples of three or five are considered in the sum, e.g. 3, 5, 6, 9, 10, 12, 15 for n=17


number = int(input("Enter a number: "))

sum = 0 

for i in range(1, number+1):
    if i % 3 == 0 or i % 5==0:
        # print(i)
    # print(multiple_of_three)
        sum += i
    # print(i)

print("Sum of the number series: ", sum)
