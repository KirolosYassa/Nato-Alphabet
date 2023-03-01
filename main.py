import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

alphabet_code = {row.letter: row.code for (index, row) in df.iterrows()}
print(alphabet_code)


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_code():
    user_input = input("Enter a word?:  ").upper()
    word = [letter for letter in user_input]
    print(word)
    try:
        nato_code = [alphabet_code[letter] for letter in word]
    except KeyError:
        print("Sorry, Only letters in the alphabet format.")
        generate_code()
    else:
        print(nato_code)

generate_code()