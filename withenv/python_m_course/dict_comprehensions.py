def run():
    # Initial Solution
    # my_dict = {}
    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         my_dict[i] = i**3

    # Dict Comprehensions
    # {key: value for value in iterable if condition}
    my_dict = {i: i**3 for i in range(1, 101) if i % 3 != 0}
    print(my_dict)
    print()

    root_sq = {i: round(i**0.5, 4) for i in range(1, 1001)}
    print(root_sq)

if __name__ == '__main__':
    run()