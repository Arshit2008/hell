import pickle
workers={}
with open('salary.pkl', 'ab') as f:  
    ask = input('do you want to add records? (y/n): ')
    if ask == 'y':
        ans = 'y'
    else:
        ans = 'n'
    while ans == 'y':
        name = input('name: ')
        emp_id = input('emp_id: ')    
        salary = input('salary: ')
        print()
        workers['emp_id'] = emp_id
        workers['name'] = name           
        workers['salary'] = salary
        pickle.dump(workers, f)          
        ans = input('Do you want to add more records? (y/n): ') 
        if ans =='n':
            break
        print()
        
with open('salary.pkl', 'rb') as f:
    find = False
    emp_id = input('Enter the employee ID to search for: ')
    while True:
        try:
            data = pickle.load(f) 
            if data['emp_id'] == emp_id:
                print('Employee found:')
                print(data) 
                find = True
                break
        except EOFError: 
            if not find:
                print('Employee ID not found.')
            print('End of Program.')
            break
        
with open('salary.pkl', 'rb') as f:
    ask = input('do you want to update data : (y/n): ')
    if ask == 'y':
        ans = 'y'
    else:
        ans = 'n'
    while ans == 'y':
        emp_id = input('Enter the employee ID to update: ')
        updated = False
        data_list = []
        while True:
            try:
                data = pickle.load(f) 
                if data['emp_id'] == emp_id:
                    print('Employee found:')
                    print(data) 
                    name = input('Enter new name: ')
                    salary = input('Enter new salary: ')
                    data['name'] = name
                    data['salary'] = salary
                    updated = True
                data_list.append(data)
            except EOFError: 
                if not updated:
                    print('Employee ID not found.')
                print('End of Program.')
                break
        with open('salary.pkl', 'wb') as f:
            for item in data_list:
                pickle.dump(item, f)
        ans = input('Do you want to update more records? (y/n): ') 
        if ans =='n':
            break
        print()   