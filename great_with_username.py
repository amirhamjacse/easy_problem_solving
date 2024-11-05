#Write a program that asks the user for their name and greets them with their name.

username = str(input("Enter your name: "))

print("Good morning", username)


#Modify the previous program such that only the users Alice and Bob are greeted with their names.

username = str(input("Enter your name: "))

if username ==  "Alice" or username == "Bob":
    print("Good morning", username)
