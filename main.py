"""Menu-driven test program for the four stack and queue implementations."""

from array_stack import ArrayStack
from linked_stack import LinkedStack
from array_queue import ArrayQueue
from linked_queue import LinkedQueue
from applications import is_balanced, print_queue_demo


def show_state(structure):
    print("Current state:", structure)


def stack_menu(stack):
    while True:
        print("\n1. Push  2. Pop  3. Peek  4. Is empty?  5. Is full?  0. Back")
        choice = input("Choose an operation: ").strip()
        try:
            if choice == "1":
                value = input("Value to push: ")
                stack.push(value)
                show_state(stack)
            elif choice == "2":
                print("Removed:", stack.pop())
                show_state(stack)
            elif choice == "3":
                print("Top element:", stack.peek())
            elif choice == "4":
                print("Is empty:", stack.is_empty())
            elif choice == "5":
                print("Is full:", stack.is_full())
            elif choice == "0":
                break
            else:
                print("Invalid choice. Try again.")
        except (IndexError, OverflowError, ValueError) as error:
            print("ERROR:", error)
            show_state(stack)


def queue_menu(queue):
    while True:
        print("\n1. Enqueue  2. Dequeue  3. Peek front  4. Is empty?  5. Is full?  0. Back")
        choice = input("Choose an operation: ").strip()
        try:
            if choice == "1":
                value = input("Value to enqueue: ")
                queue.enqueue(value)
                show_state(queue)
            elif choice == "2":
                print("Removed:", queue.dequeue())
                show_state(queue)
            elif choice == "3":
                print("Front element:", queue.peek_front())
            elif choice == "4":
                print("Is empty:", queue.is_empty())
            elif choice == "5":
                print("Is full:", queue.is_full())
            elif choice == "0":
                break
            else:
                print("Invalid choice. Try again.")
        except (IndexError, OverflowError, ValueError) as error:
            print("ERROR:", error)
            show_state(queue)


def main():
    while True:
        print("\n=== STACKS AND QUEUES: ARRAY VS. LINKED LIST ===")
        print("1. ArrayStack")
        print("2. LinkedStack")
        print("3. Circular ArrayQueue")
        print("4. LinkedQueue")
        print("5. Check balanced parentheses")
        print("6. Run print queue simulation")
        print("0. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            capacity = int(input("Enter stack capacity: "))
            stack_menu(ArrayStack(capacity))
        elif choice == "2":
            stack_menu(LinkedStack())
        elif choice == "3":
            capacity = int(input("Enter queue capacity: "))
            queue_menu(ArrayQueue(capacity))
        elif choice == "4":
            queue_menu(LinkedQueue())
        elif choice == "5":
            expression = input("Enter an expression using (), [], or {}: ")
            print("Balanced." if is_balanced(expression) else "Not balanced.")
        elif choice == "6":
            print_queue_demo()
        elif choice == "0":
            print("Program ended.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
