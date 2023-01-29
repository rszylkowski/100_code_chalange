"""
Caesar Cipher
"""
import cripting_functions
import common_func as cf
from logo import logo

print(logo)

keep_going = True

while keep_going:
    option_select = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    if option_select == "encode":
        print(f"The {option_select}d text is {cripting_functions.caesar(cf.get_text(), cf.get_shift(), False)}")
    elif option_select == "decode":
        print(f"The {option_select}d text is {cripting_functions.caesar(cf.get_text(), cf.get_shift())}")

    keep_going_input = input("Type 'yes' if you want to go again. Otherwise type 'no':\n")

    if keep_going_input == "no":
        keep_going = False
        print("Goodbye")
