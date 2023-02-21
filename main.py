import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

alphabet_code = {row.letter: row.code for (index, row) in df.iterrows()}
print(alphabet_code)


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word?:  ")
word = [letter.upper() for letter in user_input]
print(word)

nato_code = [alphabet_code[letter] for letter in word if letter in alphabet_code]
print(nato_code)