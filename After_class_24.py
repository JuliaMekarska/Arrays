array = list(input("Enter the array: "))
number = float(input("Enter the number: "))
array_floats = []
count = 0

for x in array:
    
    array_floats.append(float(x))
    
for element in range(0, len(array_floats)):
    
    if number < array_floats[element]:
        
        count += 1
        
print(count)
        