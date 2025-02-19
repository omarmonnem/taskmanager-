def view():
    print('Viewing tasks:')
    with open ('tasks.txt', 'r' , encoding='utf-8') as file:
        tasks=file.readlines()
    i=1
    for  line  in tasks:
        print(i,'- ', line)
        i+=1 #i=i+1 
           
    menu()


def delete():
    print('Deleting task:')
    #View all tasks
    with open ('tasks.txt', 'r' , encoding='utf-8') as file:
        tasks=file.readlines()
    i=1
    for  line  in tasks:
        print(i,'- ', line)
        i+=1 #i=i+1
    #let user enter task
    task_ID =int(input('Enter task ID to be delete: '))     #to get int 
    if task_ID > len(tasks) :              # if user get 
        print ("task not found")            #
    else :                                 #
        del tasks[task_ID-1]
        print('Task ID (',+task_ID,') has been deleted successfully.')
    #Rewrite tasks into file
        with open ('tasks.txt','w',encoding='utf-8') as file:
            file.writelines(tasks)
        print('Tasks have been updated succesfully')
    menu()




def add():
    print('Adding a task...')
    task_name=input('Enter task: ')
    with open('tasks.txt', 'a', encoding='utf-8') as file:
        file.write(task_name + '\n')
    print('Task added successfully!')
    menu()

def menu():
    print('Menu:')
    print('1. View tasks')
    print('2. Add a task')
    print('3. Delete a task')
    print('4. Exit')
    choice = input('Enter choice: ')
    if choice == '1':
        view()
    elif choice == '2':
        add()
    elif choice == '3':
        delete()
    elif choice == '4':
        return
    else :          #if user get 
        print ("not found")          #if user get 
        

if __name__ == '__main__':
    menu()