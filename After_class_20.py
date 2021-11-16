number = int(input("Enter the number: "))
array = list(input("Enter the array: "))
array_ints = []

def occurs(number, array):

    print("Number: ", number)

    for x in array:
        
        array_ints.append(int(x))
        
    print("Array: ", array_ints)

    for i in array_ints:
    
        if i == number:
        
            x = print(f"Result: number {number} appears in the array")
            return x
        
        else:
        
            y = print(f"Result: number {number} doesn't appear in the array")
            return y
    
print(occurs(number, array))