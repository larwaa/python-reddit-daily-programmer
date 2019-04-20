def upc(string):
    while len(string) != 11:
        string = "0" + string

    sum = 0

    for c in string[::2]:
        sum += int(c)

    sum *= 3

    for c in string[1::2]:
        sum += int(c)

    m = sum % 10

    if m == 0:
        return 0

    return 10 - m


def main():
    print(upc("3600029145"))
    print(upc("12345678910"))
    print(upc("00001234567"))

main()