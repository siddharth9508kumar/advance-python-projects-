#Define a function that accepts 2 values and return its sum, subtraction and multiplication. 
def sum_sub_mul(a, b):
    sum_result = a + b
    sub_result = a - b
    mul_result = a * b
    return sum_result, sub_result, mul_result
input1 = float(input("Enter first number: "))
input2 = float(input("Enter second number: "))
result = sum_sub_mul(input1, input2)
print(f"Sum: {result[0]}, Subtraction: {result[1]}, Multiplication: {result[2]}")
