from ArrayStack import ArrayStack
from DequeStack import DequeStack
from LinkedListStack import LinkedListStack
from ArrayQueue import ArrayQueue
from LinkedListQueue import LinkedListQueue
from CircularQueue import CircularQueue


class Main:
    def __init__(self):
        self.stack = None
        self.queue = None
        self.stack_types = {"1": ArrayStack, "2": LinkedListStack, "3": DequeStack}
        self.queue_types = {
            "4": ArrayQueue,
            "5": LinkedListQueue,
            "6": CircularQueue,
        }

    def select_stack(self):
        print("Select the type of Stack you want to use:")
        print("1. ArrayStack")
        print("2. LinkedListStack")
        print("3. DequeStack")

        choice = input("Enter your choice (1, 2, or 3): ")
        print()
        capacity = 5

        if choice in self.stack_types:
            self.stack = self.stack_types[choice](capacity)
            print(
                f"{self.stack.__class__.__name__} has been selected with capacity {capacity}.\n"
            )
        else:
            print("Invalid choice. Please select a valid option.\n")

    def select_queue(self):
        print("Select the type of Queue you want to use:")
        print("4. ArrayQueue")
        print("5. LinkedListQueue")
        print("6. CircularQueue")

        choice = input("Enter your choice (4, 5, or 6): ")
        print()
        max_size = 5

        if choice in self.queue_types:
            self.queue = self.queue_types[choice](max_size)
            print(
                f"{self.queue.__class__.__name__} has been selected with max size {max_size}.\n"
            )
        else:
            print("Invalid choice. Please select a valid option.\n")

    def run(self):
        while True:
            print("Select an option:")
            print("1. Use Stack")
            print("2. Use Queue")
            print("3. Exit")

            choice = input("Enter your choice (1, 2, or 3): ")
            print()

            if choice == "1":
                self.select_stack()
                self.run_stack_operations()
            elif choice == "2":
                self.select_queue()
                self.run_queue_operations()
            elif choice == "3":
                print("Exiting program.\n")
                break
            else:
                print("Invalid choice. Please select a valid option.")

    def run_stack_operations(self):
        while True:
            print("\nStack Operations:")
            print("1. Push")
            print("2. Pop")
            print("3. Check if Empty")
            print("4. Check if Full")
            print("5. View Top")
            print("6. Return to Main Menu")

            choice = input("Enter your choice: ")
            print()

            if choice == "1":  # Push
                item = input("Enter the item to push: ")
                print()
                try:
                    self.stack.push(item)
                    print(f"Item '{item}' pushed to stack.")
                except Exception as e:
                    print(f"{str(e)}\n")

            elif choice == "2":  # Pop
                try:
                    item = self.stack.pop()
                    print(f"Item '{item}' popped from stack.")
                except Exception as e:
                    print(f"{str(e)}\n")

            elif choice == "3":  # Check if Empty
                print(
                    "Stack is empty.\n"
                    if self.stack.is_empty()
                    else "Stack is not empty.\n"
                )

            elif choice == "4":  # Check if Full
                print(
                    "Stack is full.\n"
                    if self.stack.is_full()
                    else "Stack is not full.\n"
                )

            elif choice == "5":  # View Top
                try:
                    print(f"Top item: {self.stack.top()}")
                except Exception as e:
                    print(f"{str(e)}\n")

            elif choice == "6":  # Return to Main Menu
                print("Returning to Main Menu.\n")
                break

            else:
                print("Invalid choice. Please select a valid option.")

    def run_queue_operations(self):
        while True:
            print("\nQueue Operations:")
            print("1. Enqueue")
            print("2. Dequeue")
            print("3. Check if Empty")
            print("4. Check if Full")
            print("5. View Front")
            print("6. Return to Main Menu")

            choice = input("Enter your choice: ")
            print()

            if choice == "1":  # Enqueue
                item = input("Enter the item to enqueue: ")
                print()
                try:
                    self.queue.enqueue(item)
                    print(f"Item '{item}' enqueued.")
                except Exception as e:
                    print(f"{str(e)}\n")

            elif choice == "2":  # Dequeue
                try:
                    item = self.queue.dequeue()
                    print(f"Item '{item}' dequeued.")
                except Exception as e:
                    print(f"{str(e)}\n")

            elif choice == "3":  # Check if Empty
                print(
                    "Queue is empty.\n"
                    if self.queue.is_empty()
                    else "Queue is not empty.\n"
                )

            elif choice == "4":  # Check if Full
                print(
                    "Queue is full.\n"
                    if self.queue.is_full()
                    else "Queue is not full.\n"
                )

            elif choice == "5":  # View Front
                try:
                    print(f"Front item: {self.queue.get_front()}")
                except Exception as e:
                    print(f"{str(e)}\n")

            elif choice == "6":  # Return to Main Menu
                print("Returning to Main Menu.\n")
                break

            else:
                print("Invalid choice. Please select a valid option.")


main = Main()
main.run()
