array = list(input("Enter the array: "))
array_ints = []

def minmax(array):
    
    for x in array:
        
        array_ints.append(int(x))
        
    a = min(array_ints)
    b = max(array_ints)

    return a, b

print(minmax(array))