upper_count = 0
lower_count = 0
def func(char):
    global upper_count
    global lower_count
    
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1

file = open("OP.txt", "r")   
text = file.read()          
file.close() 
                
for char in text:
    func(char)
    
print("Uppercase letters:", upper_count)
print("Lowercase letters:", lower_count)