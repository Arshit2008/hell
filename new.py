a = 0
def counter (num):
    global a
    a += len(num)
    
f = open('Students.txt','w+')
for i in range (3):
    name = f.write(input('Enter the name: '))
    dash = f.write('-')
    rolNo= f.write(input('Enter the Roll Number: '))
    print()
    f.write('\n')

f.seek(0)
string = f.read().split()
for i in string:
    counter(i)
f.seek(0)
q = f.readlines()
print('Number of Bytes',a)
print('Number of students is : ',len(q))

f.close()
