#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - insertsa number into a sorted singly linked list
 * @head: list head
 * @number: An integer
 *
 * Return: the address of the new node, or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = NULL, *cursor = NULL, *tmp = NULL;

	if (!head)
		return (NULL);

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;

	cursor = *head;
	while (cursor && cursor->n < number)
	{
		tmp = cursor;
		cursor = cursor->next;
	}

	new_node->next = cursor;
	if (tmp)
		tmp->next = new_node;
	else
		*head = new_node;

	return (new_node);
}
