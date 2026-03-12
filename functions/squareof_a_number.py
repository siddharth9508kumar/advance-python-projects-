#6. Write a program that appends the square of each number to a new list.  
def square_of_numbers(numbers):
    squared_list = []
    for num in numbers:
        squared_list.append(num ** 2)
    return squared_list
input_numbers = input("Enter numbers separated by spaces: ")
numbers_list = list(map(int, input_numbers.split()))
squared_numbers = square_of_numbers(numbers_list)
print(f"The squares of the numbers {numbers_list} are: {squared_numbers}.")
