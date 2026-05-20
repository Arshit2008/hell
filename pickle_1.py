import pickle
stu={}
with open('data.pkl', 'wb') as f:          #we are opening the file in write binary mode
    ans = 'y'
    while ans:
        name = input('name: ')
        roll_no = input('roll_no: ')    #we are taking all the inputs
        marks = input('marks: ')
        print()
        stu['roll_no'] = roll_no
        stu['name'] = name           #we are storing the inputs in a dictionary
        stu['marks'] = marks
        pickle.dump(stu, f)          #we are dumping the dictionary in the file
        ans = input('Do you want to add more records? (y/n): ') #we are asking the user if they want to add more records
        if ans =='n':
            break
        print()
with open('data.pkl', 'rb') as f: #we are opening the file in read binary mode
    while True:
        try:
            data = pickle.load(f) #we are loading the data from the file
            print(data) 
        except EOFError: #we are catching the end of file error
            break