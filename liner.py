def func(char):
    char = char.strip()
    char = list(char)
    symbol = ',!.?'  
    
    if char[-1] in symbol:
        print(char[-1],'is a symbol')
    else:
        print('no')
        
        
f = open('OP.txt','r')
text = f.readlines()
f.close()

print(text)
for char in text:
    func(char)
f.close()