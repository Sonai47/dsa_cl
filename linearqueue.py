size = int(input("Enter your size:"))
queue = [0] * size
front = -1
rear = -1

while True:
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")

    choice = int(input("ENter your choice: "))

    if choice == 1:
        if rear == size - 1:
            print("queue overflow")
        else:
            ele = int(input("Enter your value: "))

            if front == -1:
                front = 0

            rear = rear+1
            queue[rear] = ele

    elif choice == 2:
        if front > rear or  front == -1:
            print("Underflow")
        else:
            print("delete element")
            front = front + 1

    elif choice == 3:
        print(queue)

    else:
        break