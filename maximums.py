def max_of_two(x, y):
    if x > y:
        return x
    else:
        return y

def max_of_three(x, y, z):
    return max_of_two(x, max_of_two(y, z))
print(max_of_two(5,4))
print(max_of_two(-2,-3)) 
print(max_of_two(0,0)) 
print(max_of_three(5,4,7)) 
print(max_of_three(-2,-3,-1)) 
print(max_of_three(0,0,0)) 