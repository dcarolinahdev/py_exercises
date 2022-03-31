def run():
    # Initial Solution
    # squares = []
    # for i in range(1, 101):
    #     # only not divisible by 3
    #     if i % 3 != 0:
    #         squares.append(i**2)

    # List Comprehensions
    # [element for element in iterable if condition]
    squares = [i**2 for i in range(1, 101) if i % 3 != 0]
    print(squares)
    print()

    # mcm1 = [i for i in range(1, 100000) if (i % 4 == 0 and i % 6 == 0 and i % 9 == 0)]
    mcm2 = [i for i in range(1, 100000) if i % 36 == 0]
    print(mcm2)


if __name__ == '__main__':
    run()