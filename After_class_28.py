array = [1, 23, 5, 382, 1, 17, 4, 906]

size = len(array)

print('-' * (size * 6))

for number in array:
    
    char_size = len(str(number))
    
    print("|", " " * (4 - char_size), number, "|", sep = "", end = "")

print()
print('-' * (size * 6))