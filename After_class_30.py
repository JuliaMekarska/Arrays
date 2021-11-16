import random
array = list(input("Enter the array: "))

def rand_elem(array):
    
    x = random.choice(array)
    return x
    
print(rand_elem(array))
    