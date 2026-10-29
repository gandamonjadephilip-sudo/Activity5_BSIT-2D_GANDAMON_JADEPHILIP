# Analysis

A linked-list stack pushes at the head because the new node can become the top immediately without searching through the list. Pushing or popping at the head takes O(1) time. If we used the tail of a singly linked list, removing the last node would require searching for the node before it and could take O(n) time. An array queue must be circular so that spaces left by removed items at the beginning can be reused. The modulo operator lets the front and rear positions wrap around to the start of the array.
