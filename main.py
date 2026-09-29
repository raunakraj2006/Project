tasks=[]

while True:
    print("\n================TO-Do LIST=================")
    print("1. Add Task")
    print("2.View Tasks")
    print("3.Marks Task Completed")
    print("4.Delete Task")
    print("5. Exit")


    choice=input("Enter your choice: ")

    #Add Task
    if choice=="1":
        task=input("Enter your task: ")

        tasks.append({
            "task":task,
            "completed": False
        })

        print("Task added succesfully.")

    #View Tasks
    elif choice== "2":
        if len(tasks)==0:
            print("No tasks found.")
        else:
            print("\n------Your Tasks------")

            for i,task in enumerate(tasks,1):
                if task["completed"]==True:
                    status="Completed"
                else:
                    status:"Pending"

                print(i,"|", task["task"])   

    #Mark Task Complete
    elif choice== "3":
        if len(tasks)== 0:
            print("No tasks found.")
        else:
            for i,task in enumerate(tasks,1):
                print(i,"|", task["task"])

            number=int(input("enter task number to mark completed:")) 


            if 1<=number<=len(tasks):
                tasks[number -1]["completed"]=True
                print("Task marked as completed.")
            else:
                print("Invalid task numner.")

    #Delete Task
    elif choice =="4":
        if len(tasks)==0:
            print("No tasks found.")
        else:
            for i,task in enumerate(tasks,1):
                print(i,"|", task["task"])

            number=int(input("Enter task number to delete:"))


            if 1<=number<=len(tasks):
                deleted=tasks.pop(number -1)
                print("Deleted task:", deleted["task"])
            else:
                print("Invalid task number.")

    #Exit
    elif choice =="5":
        print("Thank you for using To-Do List!")
        break 
    else:
        print("Invalid Choice!")                     

