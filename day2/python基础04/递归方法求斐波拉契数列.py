def foo(n):
    if n==1 or n==2:
        return 1
    return foo(n-1) +foo(n-2)
print(foo(30))
