#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * is_palindrome - function in C that checks if
 *	a singly linked list is a palindrome.
 * @head: pointer
 * Return: 0 , 1 or -1
 */
int is_palindrome(listint_t **head)
{
	listint_t *ptr;
	int i, *cpy, j;

	if (!*head || !head)
		return (1);

	ptr = *head;
	for (j = 1; ptr->next; j++)
		ptr = ptr->next;

	cpy = malloc(sizeof(int) * (j));
	if (!cpy)
		return (-1);

	for (i = 0, ptr = *head; i < j; i++, ptr = ptr->next)
		cpy[i] = ptr->n;

	for (i = 0; i < (j / 2); i++)
		if (cpy[i] != cpy[j - 1 - i])
		{
			free(cpy);
			return (0);
		}
	free(cpy);
	return (1);
}
