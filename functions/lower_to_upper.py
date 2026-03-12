# Define a function that accepts lowercase words and returns uppercase words. 
def lower_to_upper(word):
    return word.upper()
input_word = input("Enter a lowercase word: ")
upper_word = lower_to_upper(input_word)
print(f"The uppercase version of '{input_word}' is: '{upper_word}'.")
