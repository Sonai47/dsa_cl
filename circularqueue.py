size = int(input("Enter your size: "))
queue = [0]*size
front = -1
rear = -1

while True:
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        if (rear + 1)%size == front:
            print("overfow")
        else:
            x = int(input("enter your value: "))

            if front == -1:
                front = 0
                rear = 0
            else:
                rear = (rear+1)%size

            queue[rear] = x

    elif choice == 2:
        if front == -1:
            print("underflow")
        else:
            if front == rear:
                front = -1
                rear = -1
            else:
                front = (front+1)%size

    elif choice == 3:
        print(queue)
    else:
        break
