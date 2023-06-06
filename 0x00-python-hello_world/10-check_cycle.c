#include "lists.h"

/**
 * check_cycle - function in C that checks if a
*	singly linked list has a cycle in it.
 * @list: linkedlist
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *l1, *l2;

	if (!list || !list->next)
		return (0);

	l1 = list->next;
	l2 = list->next->next;
	while (l1 && l2 && l2->next)
	{
		if (l1 == l2)
			return (1);

		l1 = l1->next;
		l2 = l2->next->next;
	}
	return (0);
}
