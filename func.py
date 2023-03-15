# -------------------------------------- Task 1 -----------------------------------
def add(x, y):
    return x + y

# TODO: Add definitions of sub(), div(), mult(), exp(), as well as neg() and sqrt().
#       neg() should return the negation of the given number, and sqrt() should
#       return the square root of the given number. 

def sub(x, y):
    return x - y

def div(x, y):
    return x / y

def mult(x, y):
    return x * y

def exp(x, y):
    return x ** y 

def neg(x):
    return -x

def sqrt(x):
    return x ** 0.5

# -------------------------------------- Task 2 -----------------------------------

# TODO: Implement the quadratic formula using *only* the functions defined here.
#       Do not use arithmetic operators directly. 
#       You're allowed to define other functions.
a = 3
b = -1
c = 5

discriminant = sqrt(sub(exp(b, 2), mult(mult(4, a), c)))
numerator1 = add(neg(b), discriminant)
numerator2 = sub(neg(b), discriminant)
denominator = mult(2, a)
x1 = div(numerator1, denominator)
x2 = div(numerator2, denominator)

arithx1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2*a)  
arithx2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2*a) 

print("Non Arithmetic calc - First root:" + str(x1))
print("Non Arithmetic calc - Second root:" + str(x2))

print("Arithmetic calculation:" + str(arithx1))
print("Arithmetic calculation:" + str(arithx2))