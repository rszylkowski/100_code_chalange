def get_text():
    return input("Type your message:\n").lower()


def get_shift():
    shift = int(input("Type the shift number:\n"))
    if shift >= 25:
        shift %= 25
    return shift
