def fibonacci_series(n):
   
    a, b = 0, 1
    series = []
    
    
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    
    return series


num_terms = 10
fib_series = fibonacci_series(num_terms)
print(f"The first {num_terms} terms of the Fibonacci series are: {fib_series}")