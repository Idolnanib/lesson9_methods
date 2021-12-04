



def kvadrat(a):
    return a*a

# сложнеие
def addition(a, b):
    return a+b

def delit(a,b):
    return a/b



x = int(input("Enter x: "))
y = int(input("Enter y: "))
z = int(input("Enter z: "))

# (x^2)^2
print(kvadrat(kvadrat(x)))

# (x^2+y)/z

print(delit(addition(kvadrat(x), y), z))