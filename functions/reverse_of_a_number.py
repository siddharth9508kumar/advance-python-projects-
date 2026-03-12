#. Write a Python program to reverse a number. 
def reverse_number(num):
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = (reversed_num * 10) + digit
        num //= 10
    return reversed_num
number_input = int(input("Enter a number to reverse: "))
reversed_result = reverse_number(number_input)
print(f"The reverse of the number {number_input} is: {reversed_result}.")
