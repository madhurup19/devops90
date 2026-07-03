tasks = []

while True:
    print("\n=== AI SMART STUDY PLANNER ===")
    print("1.Add study Task")
    print("2.View Tasks")
    print("3.Exit")

    choise = input("Choose option:")

    if choise == "1":
        task = input("Entry study task:")
        tasks.append(task)
        print("Task Added")

    elif choise == "2":
        if len(tasks) == 0:
            print("No Tasks Found")

        else:
            print("\nYour Study Tasks:")
            for i in range(len(tasks)):
                print(i + 1, "_",tasks[i])
           
    elif choise == "3":
        print("Planner Closed")
        break
    else:
        print("Invalid Option")
