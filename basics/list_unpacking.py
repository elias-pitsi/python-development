# List unpacking 

def concat(*args, sep="/"):
    return sep.join(args)

print(concat("earth", "mars", "venus"))

# Lambda exprerssions 

def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
print(f(0))
print(f(1))