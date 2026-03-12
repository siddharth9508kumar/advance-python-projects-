#Write a program to filter even and odd number from a list. 
def filter_even_odd(numbers):
    even_numbers = []
    odd_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
    return even_numbers, odd_numbers
input_numbers = input("Enter numbers separated by spaces: ")
numbers_list = list(map(int, input_numbers.split()))
even, odd = filter_even_odd(numbers_list)
print(f"Even numbers: {even}")
print(f"Odd numbers: {odd}")