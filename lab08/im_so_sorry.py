def blocks(n):
    return 0 if n <= 0 else blocks(n - 1) + n


def factorial(n):
    return 0 if n < 0 else n * factorial(n - 1)


def print_count_down(n):
    if n <= 0:
        print("BOOM")
    else:
        print(n)
        print_count_down(n - 1)


print(factorial(3))
print(factorial(5))
print(factorial(8))
print(factorial(52))
print("----------------")
print(blocks(8))
print(blocks(0))
print(blocks(-1))
print(blocks(1))
print(blocks(5))
print(blocks(10))
print("----------------")
print(print_count_down(3))
print(print_count_down(5))
print(print_count_down(30))
