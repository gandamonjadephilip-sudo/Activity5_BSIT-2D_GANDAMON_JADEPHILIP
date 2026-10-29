# Activity 5: Stacks and Queues — Array vs. Linked List

## Description
This Python program demonstrates four data structures: an array-based stack, a linked-list stack, a circular array queue, and a linked-list queue. It also includes a balanced-parentheses checker and a print queue simulation.

## Files
- `array_stack.py` — ArrayStack with push, pop, peek, is_empty, and is_full.
- `linked_stack.py` — LinkedStack implemented with nodes.
- `array_queue.py` — Circular ArrayQueue with enqueue, dequeue, peek_front, is_empty, and is_full.
- `linked_queue.py` — LinkedQueue with front and rear references.
- `applications.py` — Balanced-parentheses checker and print queue exercise.
- `main.py` — Menu-driven test driver for the implementations.
- `analysis.md` — Answer to the analysis question.
- `sample_runs.txt` — Example output for normal operations and error handling.

## Requirements
- Python 3
- No extra libraries are required.

## How to Run
1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run `python main.py`.
4. Choose an implementation from the menu and follow the prompts.

To run the application exercises directly, use `python applications.py`.

## Notes
- Array-based structures have a fixed capacity and report overflow when full.
- Linked-list structures do not have a fixed capacity; available memory is the practical limit.
- Empty stack or queue operations report underflow.
- The circular array queue uses modulo (`%`) to wrap around and a size counter to distinguish full from empty.
