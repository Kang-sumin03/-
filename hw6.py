def display_multiplication_table():
    i = 1
    while i <= 9:
        for n in range(2, 6):
            print(f'{n}x{i}={n*i:2d}', end='   ')
        print()
        i = i+1

    print()

    i = 1
    while i <= 9:
        for n in range(6, 10):
            print(f'{n}x{i}={n*i:2d}', end='   ')
        print()
        i = i+1

display_multiplication_table()
