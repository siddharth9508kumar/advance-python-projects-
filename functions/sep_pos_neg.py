#WAP to separate positive and negative number from a list.  
def separate_pos_neg(numbers):
    positive_numbers = []
    negative_numbers = []
    for num in numbers:
        if num >= 0:
            positive_numbers.append(num)
        else:
            negative_numbers.append(num)
    return positive_numbers, negative_numbers
input_numbers = input("Enter numbers separated by spaces: ")
numbers_list = list(map(int, input_numbers.split()))
positive, negative = separate_pos_neg(numbers_list)
print(f"Positive numbers: {positive}")
print(f"Negative numbers: {negative}")
