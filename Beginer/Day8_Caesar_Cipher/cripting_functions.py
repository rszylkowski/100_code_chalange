alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(text, shift, decrypt=True):
    end_txt = ""

    if decrypt:
        shift *= -1

    for e in text:
        if e not in alphabet:
            end_txt += e
            continue

        alphabet_position = alphabet.index(e)

        if alphabet_position + shift > len(alphabet) - 1:
            new_letter_pos = alphabet_position + shift - len(alphabet)
            end_txt += alphabet[new_letter_pos]
            continue

        new_letter_pos = alphabet_position + shift
        end_txt += alphabet[new_letter_pos]

    return end_txt


# Two function version

# def encode_data(text, shift_number):
#     encoded_text = ""
#     for e in text:
#         if e not in alphabet:
#             encoded_text += e
#             continue
#         new_letter_position = 0
#         alphabet_position = alphabet.index(e)
#         if (alphabet_position + shift_number) <= len(alphabet) - 1:
#             new_letter_position = alphabet_position + shift_number
#         elif alphabet_position + shift_number > len(alphabet):
#             new_letter_position = alphabet_position + shift_number - len(alphabet)
#         encoded_text += alphabet[new_letter_position]
#     print(encoded_text)
#
#
# def decode_data(text, shift_number):
#     encoded_text = ""
#     for e in text:
#         if e not in alphabet:
#             encoded_text += e
#             continue
#         alphabet_position = alphabet.index(e)
#         new_letter_position = alphabet_position - shift_number
#         encoded_text += alphabet[new_letter_position]
#     print(encoded_text)
