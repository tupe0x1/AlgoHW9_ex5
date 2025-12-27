import math


def _i_function(i): return i

def _create_function(budget, i):
    return lambda j: budget * min(1, j * i)

def get_functions(budget, size):
    return [_create_function(budget, i) for i in range(1, size)]

def main():
    funcs = get_functions(100, 3)
    for func in funcs:
        print(func.__name__)
        print(func(0))
        print(func(0.25))
        print(func(0.5))
        print(func(0.75))
        print(func(1))

if __name__ == '__main__':
    main()