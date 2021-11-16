array = list(input("Enter the array: "))
array_ints = []

def f(array):
    
    for x in array:
        array_ints.append(int(x))

    y = repr(array_ints).replace("[", " ").replace("]", " ")
    
    return y

print(f(array))
        
        