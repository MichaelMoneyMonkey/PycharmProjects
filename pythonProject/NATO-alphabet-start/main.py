import pandas


#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}


data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
# 👆 {row.naam: row.naam for (afblijven, afblijven) in data.iterrows()}

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Geef een woord: ").upper()
print(user_input)

result = [phonetic_dict[letter] for letter in user_input]
print(result)
