import random

def binary_search(my_list, start, end, objetivo):
    print(f'Looking for {objetivo} between {my_list[start]} and {my_list[end]}')
    if start > end:
        return False

    medio = (start + end) // 2

    if my_list[medio] == objetivo:
        return True
    elif my_list[medio] < objetivo:
        return binary_search(my_list, medio + 1, end, objetivo)
    else:
        return binary_search(my_list, start, medio - 1, objetivo)


if __name__ == '__main__':
    size_list = int(input('How big will the list be? '))
    objetive = int(input('What number do you want to find? '))

    my_list = sorted([random.randint(0, 100) for i in range(size_list)])

    found = binary_search(my_list, 0, len(my_list)-1, objetive)
    print(my_list)
    print(f'Element {objetive} {"is" if found else "is not"} in list.')
