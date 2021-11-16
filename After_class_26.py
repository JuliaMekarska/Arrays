array1 = list(input("Enter the array: "))
array = []

def segregate(array):
    
    for x in array1:
        
        array.append(int(x))
 
    left, right = 0, len(array) -1
 
    while left < right:

        while (array[left] % 2 == 0 and left < right):
            
            left += 1
 
        while (array[right] % 2 == 1 and left < right):
            
            right -= 1
 
        if (left < right):
            
              array[left], array[right] = array[right], array[left]
              left += 1
              right -= 1

segregate(array)
print ("Array after segregation: "),
for i in range(0,len(array)):
    print(array[i])
        