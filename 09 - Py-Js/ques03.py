def pyramid(rows):

    print("pyramid:")
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * (2 * i - 1))
    print("\nreverse pyramid:")
    for i in range(rows, 0, -1):
        print(" " * (rows - i) + "*" * (2 * i - 1))
        
pyramid(5)