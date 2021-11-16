array = list(input("Enter the array: "))
array_ints = []

def power(array):
    
    for x in array:
        
        array_ints.append(int(x))
    
    print("Array: ", array_ints)
    print("2nd power: ")

    for element in array_ints:
        
        element = element ** 2
        
        print(element)
        
print(power(array))