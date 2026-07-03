tasks = []
completed = []

while True:

    print("\n===== AI SMART STUDY PLANNER =====")
    print("1. Add Study Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter study task: ")
        tasks.append(task)
        print("✅ Task Added Successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("📌 No Tasks Available!")
        else:
            print("\nYour Study Tasks:")
            for i in range(len(tasks)):
                if i in completed:
                    status = "Done"
                else:
                    status = "Pending"

                print(f"{i + 1}. {tasks[i]} - {status}")

    elif choice == "3":
        if len(tasks) == 0:
            print("📌 No Tasks Available!")
        else:
            num = int(input("Enter task number to complete: "))

            if 1 <= num <= len(tasks):
                if (num - 1) not in completed:
                    completed.append(num - 1)
                    print("✅ Task Completed!")
                else:
                    print("⚠️ Task is already completed.")
            else:
                print("❌ Invalid Task Number!")

    elif choice == "4":
        print("👋 Planner Closed.")
        break

    else:
        print("❌ Invalid Choice! Please select 1-4.")



    

