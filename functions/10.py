#Define a function in python that accepts 3 values and returns the maximum of three 
#numbers.  
def find_maximum(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
maximum = find_maximum(num1, num2, num3)
print(f"The maximum of the three numbers is: {maximum}")
