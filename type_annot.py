def func(a: int, b: int) -> int:
    """An example of type annotation in a function
    """
    return a + b


def func2(a: list, b: str) -> str:

    for x in a:
        print(f'{b} {x}')

    return 'Success'


if __name__ == '__main__':
    print(func(2,5))

    names = ['alpha', 'beta', 'gamma']
    print(func2(names, 'hello'))