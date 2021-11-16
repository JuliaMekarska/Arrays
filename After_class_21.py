array = list(input("Enter the array: "))
array_ints = []

def sec_large(array):
    
    for x in array:
        
        array_ints.append(int(x))

    array_ints.sort()
    
    x = array_ints[-2]
    
    return x

print(sec_large(array))
