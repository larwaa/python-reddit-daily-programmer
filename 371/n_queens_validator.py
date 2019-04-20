SIZE = 8


def n_queens(list):
    if len(set(list)) != len(list):
        return False


    [list[i] + i for i in range(len(list))]
    for i in range(SIZE):
        for j in range(1, SIZE - i):
            queen_row = list[i]

            next_queen_row = list[i + j]
            if queen_row + j == next_queen_row or queen_row - j == next_queen_row:
                return False
    return True


def distinct(list):
    return len(list) == len(set(list))


def enumerate_queens(list):
    enumerated = enumerate(list)
    list1 = [x - i for i, x in enumerated]
    list2 = [x + i for i, x in enumerated]
    return distinct(list) and distinct(list1) and distinct(list2)




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
