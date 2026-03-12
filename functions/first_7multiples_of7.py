# Write a program to display the first 7 multiples of 7.  
def multiples_of_seven(n):
    multiples = []
    for i in range(1, n + 1):
        multiples.append(7 * i)
    return multiples
num_multiples = 7
result = multiples_of_seven(num_multiples)
print(f"The first {num_multiples} multiples of 7 are: {result}.")
