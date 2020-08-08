a: int = 1
b: int = 2
c: str = '1'
d: str = '2'
e = 1

def add(x: int, y: int) -> int:
    return x + y

if __name__ == '__main__':
    print(add(a, b))
    print(add(c, d))
    e = '1'