def nth_fibonacci(x):
    
    if x<=1:
        return x
    
    return nth_fibonacci(x-1) + nth_fibonacci(x-2)

x = 7
result = nth_fibonacci(x)
print (result)