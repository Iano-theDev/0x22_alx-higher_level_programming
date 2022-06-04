#This is python, hello world!

For task 10.
We are looking to see if the linked list has a loop wthithin it(i.e the cycle).
This means that there no node points to NULL.
<u>Solution</u>
Create two pointers.
Use the two pointers to iterate throuth the linked list.
One of the pointers must be faster than the othe:
	-If there's a cycle in the linked list then at some point the two pointers will coilide.
	-Otherwise, there is no cycle/ loop in the linked list.
	-The first pointer will start at the second node and will move two nodes at a time.
	-The second node will start at the head node and will move one node at a time.
