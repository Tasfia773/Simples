def load_tasks():
    try:
        with open("task.txt","r") as file:
            tasks=[line.strip() for line in file.readlines()]
    except FileNotFoundError:
        tasks=[]
    return tasks
def save_task(tasks):
    with open("task.txt","w") as file:
        for t in tasks:
            file.write(t +"\n")
def show_task(tasks):
    if not tasks:
        print("No Task Yet!")
    for i,task in enumerate(tasks,1):
        print(f"{i}.{task}")
def main():
    tasks=load_tasks()
    while(True):
        print("operation : Add View delete quit")
        choice=input("Enter You Choice : ").lower()
        if choice=="view":
            show_task(tasks)
        elif choice=="add":
            task=input("Enter New Task : ")
            tasks.append(task)
            save_task(tasks)
        elif choice =="delete":
            show_task(tasks)
            task_num=int(input("Enter Task No.To Delete : "))
            if 0<task_num<=len(tasks):
                tasks.pop(task_num-1)
                save_task(tasks)
            else:
                print("Bhul Hoise Apnar")
        elif choice=="quit":
            print("Hoie Gese Apnar Ebar Jan")
            break
        else:
            print("ki Choice Korli Bhai")
if __name__=="__main__":
    main()


        