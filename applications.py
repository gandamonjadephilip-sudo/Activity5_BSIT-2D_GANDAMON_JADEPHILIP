"""Application exercises: balanced parentheses and print queue simulation."""

from array_stack import ArrayStack
from array_queue import ArrayQueue


def is_balanced(expression):
    """Return True when (), [], and {} are correctly matched."""
    stack = ArrayStack(max(1, len(expression)))
    matching_open = {")": "(", "]": "[", "}": "{"}
    opening = set(matching_open.values())

    for character in expression:
        if character in opening:
            stack.push(character)
        elif character in matching_open:
            if stack.is_empty() or stack.pop() != matching_open[character]:
                return False

    return stack.is_empty()


def print_queue_demo():
    """Add printing jobs and process them in FIFO order."""
    queue = ArrayQueue(5)
    jobs = [
        {"id": "JOB-101", "pages": 3},
        {"id": "JOB-102", "pages": 8},
        {"id": "JOB-103", "pages": 2},
    ]

    print("\nPRINT QUEUE SIMULATION")
    for job in jobs:
        queue.enqueue(job)
        print(f"Added {job['id']} ({job['pages']} pages). {queue}")

    print("\nProcessing jobs in FIFO order:")
    while not queue.is_empty():
        job = queue.dequeue()
        print(f"Printing {job['id']} - {job['pages']} pages. Remaining: {queue}")


def parentheses_demo():
    print("\nBALANCED PARENTHESES CHECKER")
    expression = input("Enter an expression using (), [], or {}: ")
    if is_balanced(expression):
        print("The parentheses are balanced.")
    else:
        print("The parentheses are NOT balanced.")


if __name__ == "__main__":
    parentheses_demo()
    print_queue_demo()
