#Write a program that asks the user for a number n and gives them the possibility to choose between computing the sum and computing the product of 1,…,n.

n = int(input("Enter number series: "))
print("select", "1", "to", n)
sum_of_series = int(input("Enter sum of number: "))
print("select", "1", "to", n)
product_of_series = int(input("Enter product number: "))

sum_n = 0
prod_n = 1
if sum_of_series <= n:
    for i in range(1, sum_of_series+1):
        sum_n += i
else:
    print("Error")
print(sum_n)

if product_of_series <= n:
    for j in range(1, product_of_series+1):
        # print(j, 'works')
        prod_n *= j
else:
    print("Error")
print(prod_n)
