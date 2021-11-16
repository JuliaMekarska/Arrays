array1 = list(input("Enter the first array: "))
array2 = list(input("Enter the second array: "))
a = len(array1)
b = len(array2)

def Subset(array1, array2, a, b):
    
    element1 = 0
    element2 = 0
    
    for element2 in range(a):
        
        for element1 in range(b):
            
            if(array1[element2] == array2[element1]):
                
                break

        if (element1 == b):
            
            y = print("The first array is the subset of the second array")
            
            return y

    x = print("The first array isn't the subset of the second array")

    return x

print(Subset(array1, array2, a, b))