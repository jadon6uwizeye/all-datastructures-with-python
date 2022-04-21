def fibonacci(n):
    a = 0
    b = 1
    for counter in range(n):
        yield a 
        a, b = b, a+b
        
for f in fibonacci(10):
    print(f)