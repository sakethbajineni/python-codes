def fibonacci_series(n):
    if n<=1:
        return n 
    else:
        return fibonacci_series(n-1)+fibonacci_series(n-2)
n=int(input())
result=fibonacci_series(n)
print(result)