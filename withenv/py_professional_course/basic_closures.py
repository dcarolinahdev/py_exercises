from timeit import repeat


def make_multiplier(x):

    def multiplier(n):
        return x * n

    return multiplier

times10 = make_multiplier(10)
times4 = make_multiplier(4)

"""
print(times10(3))
print(times4(5))
print(times10(times4(2)))
"""

def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, "You only can use strimgs"
        return string * n
    return repeater

def run():
    repeat_5 = make_repeater_of(5)
    # print(repeat_5("Hola"))
    repeat_10 = make_repeater_of(10)
    # print(repeat_10("Platzi"))

if __name__ == '__main__':
    run()
