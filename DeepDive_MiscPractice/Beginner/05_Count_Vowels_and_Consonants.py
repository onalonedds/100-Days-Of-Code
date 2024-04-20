vowels = ('a', 'e', 'i', 'o', 'u')
consonants = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z')
num_vowels = num_consonants = 0

user_string = input('String to count vowels and consonants: ').lower()

for char in user_string:
    num_vowels = char in vowels and num_vowels + 1 or num_vowels
    num_consonants = char in consonants and num_consonants + 1 or num_consonants

print(f'Vowels: {num_vowels}, consonants: {num_consonants}')
