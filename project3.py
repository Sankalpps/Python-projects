task=[]
print("Welcome to task manager")
input("Enter the name ")
task_number=int(input("How many task do you want to add "))
for i in range(1, task_number+1):
    task_name=input(f"Task Number {i} is :")
    task.append(task_name)
while True:
    task_value=int(input("Choose any one\n1.Add\n2.Update\n3.Delete\n4.View\n5.Exit"))
    if task_value==1:
        add=input("What do you want to add")
        task.append(add)
        print(f"The task {add} has been inserted.....")
    elif task_value==2:
        updated_val=input("Enter the task to be updated")
        if updated_val in task:
            up=input("Enter the new task=")
            ind=task.index(updated_val)
            task[ind]=up
            print(f"Updated task {up}")
    elif task_value==3:
        deleted_val=input("Enter the task to be deleted")
        if deleted_val in task:
            de=task.index(deleted_val)
            del task[de]
            print(f"The task {de} deleted ")
    elif task_value==4:
        print(f"Total tasks = {task}")
    elif task_value==5:
        print("Closing The Program")
        break
    else:
        print("Invalid Input")
        