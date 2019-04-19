SIZE = 8


def n_queens(list):
    if len(set(list)) != len(list):
        return False

    for i in range(SIZE):
        for j in range(1, SIZE):
            el = list[i]

            if i + j < len(list):
                diagonal = list[i + j]
                if el == diagonal + j or el == diagonal - j:
                    return False
    return True


def main():
    list = [2, 5, 7, 4, 1, 8, 6, 3]
    list2 = [4, 2, 7, 3, 6, 8, 5, 1]
    list3 = [5, 3, 1, 4, 2, 8, 6, 3]
    list4 = [5, 8, 2, 4, 7, 1, 3, 6]
    list5 = [4, 3, 1, 8, 1, 3, 5, 2]
    print(n_queens(list))
    print(n_queens(list2))
    print(n_queens(list3))
    print(n_queens(list4))
    print(n_queens(list5))




main()
