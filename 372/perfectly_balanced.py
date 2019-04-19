def balanced_bonus(input):
    if len(input) == 0:
        return True

    init_count = input.count(input[0])

    for c in input:
        if input.count(c) != init_count:
            return False

    return True


def count(input):
    if input == "":
        return True

    letters_char = {}
    for c in input:
        letters_char[c] = letters_char.get(c, 0) + 1

    init_count = letters_char[input[0]]

    for key, value in letters_char.items():
        if value != init_count:
            return False

    return True


def main():
    print(balanced_bonus("xxxyyyzzz"))
    print(balanced_bonus("abccbaabccba"))
    print(balanced_bonus("xxxyyyzzzz"))
    print(balanced_bonus("abcdefghijklmnopqrstuvwxyz"))
    print(balanced_bonus("pqq"))
    print(balanced_bonus("fdedfdeffeddefeeeefddf"))
    print(balanced_bonus("www"))
    print(balanced_bonus("x"))
    print(balanced_bonus(""))

main()