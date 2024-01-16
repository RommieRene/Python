list_for_tasks = []

def add_task(task):
    list_for_tasks.append(task)

def remove_task (task):
    list_for_tasks.remove(task)

def view_task():
    for i, task in enumerate(list_for_tasks, 1):
        print(f'{1}. {task}')

def main():
    while True:
        print("\n --- To do list ---")
        print("1. Add task")
        print("2. View task")
        print("3. remove task")
        print("4. Exit")

        choice = input('Enter your choice (1/2/3/4): ')

        if choice == '1':
            task = input('Enter your choice description')
            add_task(task)
            print('task added successfuly')

        elif choice == '2':
            print('\n--- Tasks ---')
            view_task()
        elif choice == '3':
            index = int(input('Enter the task number to remove')) -1
            if 0 <= index < len(list_for_tasks):
                removed_task = list_for_tasks.pop(index)
                print(f"Removed task: {removed_task}")
            else:
                print("Invalid task number !")
        elif choice == '4':
            print('goodbye')
            break
        else:
            print('Invalid choice. Please try again')


if __name__ == '__main__':
    main()

