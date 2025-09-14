import math

def roots(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        r1 = (-b + math.sqrt(discriminant)) / (2*a)
        r2 = (-b - math.sqrt(discriminant)) / (2*a)
        return f"({r1}, {r2})"
    elif discriminant == 0:
        r = -b / (2*a)
        return f"({r})"
    else:
        return "( )"

def value_y(a, b, c, x):
    return a * x**2 + b * x + c

def _fmt_num_for_eq(n):
    if isinstance(n, float) and n.is_integer():
        return str(int(n))
    return str(n)

def to_string(a, b, c):
    parts = []
    if a != 0:
        parts.append(f"{_fmt_num_for_eq(a)} * X^2")
    if b != 0:
        parts.append(f"{_fmt_num_for_eq(b)} * X")
    if c != 0:
        parts.append(f"{_fmt_num_for_eq(c)}")
    if not parts:
        return "f(x) = 0"
    return "f(x) = " + " + ".join(parts)

def derivation(a, b, c):
    da = 2 * a
    db = b
    parts = []
    if da != 0:
        parts.append(f"{_fmt_num_for_eq(da)} * X")
    if db != 0:
        parts.append(f"{_fmt_num_for_eq(db)}")
    if not parts:
        return "f'(x) = 0"
    return "f'(x) = " + " + ".join(parts)

print(roots(1, -3, 2))
print(roots(1, -2, 1)) 
print(roots(1, 2, 3))  
print(value_y(1, -3, 2, 0)) 
print(value_y(1, -3, 2, 1)) 
print(value_y(1, -3, 2, -1)) 
print(to_string(2, -3, 1))   
print(derivation(2, -3, 1))  