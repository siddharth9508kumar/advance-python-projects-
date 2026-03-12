#Define a function which counts vowels and consonant in a word.  
def count_vowels_consonants(word):
    vowels = 'aeiouAEIOU'
    vowel_count = 0
    consonant_count = 0
    
    for char in word:
        if char.isalpha():  # Check if the character is an alphabet
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
                
    return vowel_count, consonant_count
input_word = input("Enter a word: ")
vowels, consonants = count_vowels_consonants(input_word)
print(f"The word '{input_word}' has {vowels} vowels and {consonants} consonants.")
