"""
Password Generator
"""
import random
big_let = [chr(e) for e in range(65, 91)]
sml_let = [chr(e) for e in range(97, 123)]
comb_let = sml_let + big_let
numbers = [chr(e) for e in range(48, 58)]
not_keep_symbols = "\"'"
symbols = [chr(e) for e in range(33, 44) if chr(e) not in not_keep_symbols]

print("Welcom to the PyPassword Generator!")

letters_amount = int(input("How many letters would you like in your password?\n"))
symbols_amount = int(input("How many symbol would you like?\n"))
numbers_amount = int(input("How many numbers would you like?\n"))

pass_chr_list = []
for i in range(0, letters_amount + 1):
    pass_chr_list.append(random.choice(comb_let))

for i in range(0, numbers_amount + 1):
    pass_chr_list.append(random.choice(numbers))

for i in range(0, symbols_amount + 1):
    pass_chr_list.append(random.choice(symbols))

random.shuffle(pass_chr_list)
print("".join(pass_chr_list))






