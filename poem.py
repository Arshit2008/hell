n=0
def func(string):
    vowel = 'aeiouAEIOU'
    if string[0] in vowel:
        global n
        n +=1 
f = open(r"C:\Users\lenovo 5\Music\OP.txt",'w+')
f.write("Hold fast to ypur dreams,\nfor if they die\nlife is like a broken-winged bird\nthat cannot fly")
f.seek(0)
splited = (f.read()).split('\n')
for i in splited:
    func(i)
if n>0 :
    print('lines starting with vowels',n)
else:
    print('no lines start with vowels')

f.seek(0)
ask = input('what line do you want to read: ')
length = (f.read()).split('\n')
print(length)
print(length[int(ask)-1])