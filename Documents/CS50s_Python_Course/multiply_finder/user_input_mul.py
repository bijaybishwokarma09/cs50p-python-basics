# Asking to the users for their number which he wants to find multiplication.
user_num = int(input("Enter your number here: "))

# Using the for loop for iteration the 5 and used range() method for ranging the 1 to 10 numbers.
for i in range(1, 11):
    mul = user_num * i 
# Let's print the output here is also used f string(format string) for making it more suitable.
    print(f"{user_num} * {i} = {mul} ")