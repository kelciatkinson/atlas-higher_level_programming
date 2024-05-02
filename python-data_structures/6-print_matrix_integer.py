#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for list in matrix:
        num = 1
        length = len(list)

        for i in list:
            if num == length:
                print("{}".format(i), end="")
            else:
                print("{}".format(i), end=" ")
            num += 1
        print()

