#include "lists.h"
#include <stddef.h>

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: the list
 *
 * Return: 0 if no cycle else 1
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	slow = list;
	fast = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}

