polish_names = ['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy']

def longest_name(polish_names):
    
    print("Names: ", polish_names)
    
    max1 = len(polish_names[0])
    temp = polish_names[0]
 
    for i in polish_names:
        if(len(i) > max1):
 
            max1 = len(i)
            temp = i
 
    x = ("Longest name: ", temp)
    
    return x
    
print(longest_name(polish_names))