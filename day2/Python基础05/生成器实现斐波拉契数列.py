def fib():
    i, a, b = 0, 0, 1
    while i < 10:
        yield b
        a,b = b,a+b
        i +=1
f = fib()
for i in range(5):
    print(next(f))