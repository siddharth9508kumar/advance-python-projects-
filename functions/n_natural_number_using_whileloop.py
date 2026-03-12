#Write a program to print n natural number in descending order using a while loop.  
def print_natural_numbers_descending(n):
    while n > 0:
        print(n)
        n -= 1
number = int(input("Enter a number to print natural numbers in descending order: "))
print_natural_numbers_descending(number)
print("Finished printing natural numbers in descending order.")