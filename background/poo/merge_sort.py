import random

def merge_sort(my_list):
    if len(my_list) > 1:
        half = len(my_list) // 2
        left = my_list[:half]
        right = my_list[half:]
        print(left, '*' * 5, right)

        # recursive call on each half
        merge_sort(left)
        merge_sort(right)

        # Iterators for ordering each sublists
        i = 0
        j = 0
        # Iterator for main list
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                my_list[k] = left[i]
                i += 1
            else:
                my_list[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            my_list[k] = left[i]
            i += 1
            k +=1

        while j < len(right):
            my_list[k] = right[j]
            j += 1
            k += 1
        
        print(f'left {left}, right {right}')
        print(my_list)
        print('-' * 50)

    return my_list

if __name__ == '__main__':
    size_list = int(input('How big will the list be? '))
    
    my_list = [random.randint(0, 100) for i in range(size_list)]
    print(my_list)

    ordered_list = merge_sort(my_list)
    print(ordered_list)
