#include "lists.h"

/**
 * insert_node - function in C that inserts a number into
 *	a sorted singly linked list.
 * @head: pointer
 * @number: integer
 * Return: address or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *node1 = *head;

	node = malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);
	node->n = number;

	if (node1 == NULL || node1->n >= number)
	{
		node->next = node1;
		*head = node;
		return (node);
	}

	while (node1 != NULL && node1->next != NULL && node1->next->n < number)
		node1 = node1->next;

	node->next = node1->next;
	node1->next = node;

	return (node);
}
