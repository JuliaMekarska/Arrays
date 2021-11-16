array = [2, 3, 2, 5, 8, 1, 9, 8]
unique_elements = [3, 5, 1, 9]
uniques = []

for element in array:
    
    x = False
    
    for unique_element in unique_elements:
        
        if element == unique_element:
            
            x = True
    
    if x: uniques = uniques + [element]
        
print("Array: ", *array)
print("Unique elements: ", *uniques)