def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Caro", "lastname": "Hernandez"}

    super_list = [
        {"firstname": "Cecilia", "lastname": "Lopez"},
        {"firstname": "Susana", "lastname": "Ortiz"},
        {"firstname": "Pablo", "lastname": "Gomez"},
        {"firstname": "Gabriel", "lastname": "Martinez"},
        {"firstname": "Josue", "lastname": "Smith"},
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 3, 0, 1],
        "floating_nums": [1.1, 4.55, 6.43],
    }

    for key, value in super_dict.items():
        print(key, ":", value)

    print()

    for item in super_list:
        print(item["firstname"] , ">" , item["lastname"])


if __name__ == '__main__':
    run()