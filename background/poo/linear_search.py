import random

def linear_search(my_list, objetive):
    match = False

    for element in my_list: # O(n)
        if element == objetive:
            match = True
            break

    return match


if __name__ == '__main__':
    size_list = int(input('How big will the list be? '))
    objetive = int(input('What number do you want to find? '))

    my_list = [random.randint(0, 100) for i in range(size_list)]

    found = linear_search(my_list, objetive)
    print(my_list)
    print(f'Element {objetive} {"is" if found else "is not"} in list.')
