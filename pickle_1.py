import pickle
stu={}
with open('data.pkl', 'wb') as f:
    for i in range(3):
        name = input('name: ')
        roll_no = input('roll_no:  ')
        marks = input('marks: ')
        stu['roll_no'] = roll_no
        stu['name'] = name
        stu['marks'] = marks
        pickle.dump(stu, f) 
