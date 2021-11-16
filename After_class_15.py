colors = ["red", "blue", "green", "yellow", "orange", "black", "white"]

x = open("Colors.txt", "w")

for color in colors:
    
    x.write(color)
    x.write("\n")
    
x.close()