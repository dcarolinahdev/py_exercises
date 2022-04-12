import random

def insertion_sort(my_list):

    for index in range(1, len(my_list)):
        current_value = my_list[index]
        current_position = index
        print("\n** [", current_position, "] =", current_value)

        while current_position > 0 and my_list[current_position - 1] > current_value:
            my_list[current_position] = my_list[current_position -1]
            print("  ", my_list[current_position - 1], "cambia con", current_value)
            current_position -= 1
        my_list[current_position] = current_value
        print("->", my_list)

    return my_list

if __name__ == '__main__':
    size_list = int(input('How big will the list be? '))

    my_list = [random.randint(0, 100) for i in range(size_list)]
    print(my_list)

    ordered_list = insertion_sort(my_list)
    print(ordered_list)
