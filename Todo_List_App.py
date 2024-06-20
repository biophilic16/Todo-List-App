def task():
    print("TODO LIST")
    print("---------------------------")
    no_of_task=int(input("Enter the number of tasks: "))
    tasks=[]
    for i in range(1,no_of_task+1):
        task_name=input(f"Enter task {i}: ")
        tasks.append(task_name)
    print(f"\nToday's tasks are: {tasks}")    

    while True:
        operation=int(input("\n\t1-Add\n\t2-Update\n\t3-Delete\n\t4-Veiw\n\t5-Exit\nEnter number:"))

        if operation==1:
            add=input("\nEnter the task: ")
            tasks.append(add)
            print(f"Task {add} has been successfully added...")

        elif operation==2:
            update_task=input("\nEnter the task to update: ")
            if update_task in tasks:
                update_value=input("Enter new task: ")
                ind_value=tasks.index(update_task)
                tasks[ind_value]=update_value
                print(f"Updated task: {update_value}")
            else:
                print("Not in tasks!")    

        elif operation==3:
            del_val=input("\nEnter the task to delete: ")
            if del_val in tasks:
                ind_value=tasks.index(del_val)
                del tasks[ind_value]
                print(f"The {del_val} task has been deleted...")
            else:
                print("Not in task!")    

        elif operation==4:
            print(f"\nThe tasks are {tasks}")

        elif operation==5:    
            print("\nTHANK YOU! SEE U LATER")
            print("---------------------------")

            break

        else:
            print("Invalid Input!")    

task()                

