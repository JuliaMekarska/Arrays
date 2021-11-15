def median(array):
    
    array.sort()
    
    if len(array) % 2 != 0:
        
        x = int((len(array) + 1) / 2)
        
        a = array[x - 1]
        
        return a
    
    else:
        
        y = int((len(array)/2) + (len(array)/2 + 1))
        
        b = array[y - 1] / 2
        
        return b
    
print(median([1, 0, 9, 4, 6]))