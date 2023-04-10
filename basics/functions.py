# def fib(n): 
#     """Print a Fibonacci series up to n."""
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a+b
#     print()

# print("returning from fib(2000)")
# fib(2000)

# def fib2(n): 
#     """Return a list containing the Fibonacci series up to n."""
#     result = []
#     a, b = 0, 1
#     while a < n:
#         result.append(a)    # see below
#         a, b = b, a+b
#     return result

# print("returning from fib2(3000)")
# print(fib2(3000))

# Dealing with default arguments
i = 5 
def f(arg=i):
    print(arg)

i = 6 
f() 

"""
The default value is evaluated only once. This makes a difference when the default is a mutable 
object such as a list, dictionary, or instances of most classes. For example, 
the following function accumulates the arguments passed to it on subsequent calls:
"""

# def f2(a, L=[]): 
#     L.append(a)
#     return L

# print(f2(1))
# print(f2(2))
# print(f2(3))

# Keywords argumentts 
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")
    print("type: ", type)

parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword
