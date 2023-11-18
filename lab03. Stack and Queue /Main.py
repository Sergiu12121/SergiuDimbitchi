from ArrayStack import ArrayStack
from DequeStack import DequeStack
from LinkedListStack import LinkedListStack


class Main:
    def __init__(self):
        self.stack = None
        self.stack_types = {"1": ArrayStack, "2": LinkedListStack, "3": DequeStack}

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

    def run(self):
        self.select_stack()

        while True:
            print("\nOperations:")
            print("1. Push")
            print("2. Pop")
            print("3. Check if Empty")
            print("4. Check if Full")
            print("5. View Top")
            print("6. Exit")

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
                    if self.stack.isEmpty()
                    else "Stack is not empty.\n"
                )

            elif choice == "4":  # Check if Full
                print(
                    "Stack is full.\n"
                    if self.stack.isFull()
                    else "Stack is not full.\n"
                )

            elif choice == "5":  # View Top
                try:
                    print(f"Top item: {self.stack.top()}")
                except Exception as e:
                    print(f"{str(e)}\n")

            elif choice == "6":  # Exit
                print("Exiting program.\n")
                break

            else:
                print("Invalid choice. Please select a valid option.")


main = Main()
main.run()
