def fibonacci(n):
    a = 0
    b = 1
    for counter in range(n):
        yield a 
        future = a + b
        a = b
        b = future 
for f in fibonacci(10):
    print(f)