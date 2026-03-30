# Wth the help of True 
user = input("enter you password:-")
while True:
    password = input("enter you password")
    if password == "user":
        print("login successful")
        break
    else:
        print("correct password")

'''syntax:
initialization
while condition:
    statement
    increment or decrement'''

# in for initialization is work with range and while is work manual

i = 1
while i<=5:
    print("hello proramming")
    i=i+1


# Nested while loops
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print("*", end=" ")
        j += 1
    print()
    i += 1
