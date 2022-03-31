def run():
    # Initial Solution
    squares = []
    for i in range(1, 101):
        # only not divisible by 3
        if i % 3 != 0:
            squares.append(i**2)
    print(squares)

if __name__ == '__main__':
    run()