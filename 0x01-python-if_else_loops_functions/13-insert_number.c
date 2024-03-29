#include "lists.h"

/**
 * insert_node -add  no in a sorted singly-linked list.
 * @head: A pointer the head of sorted singllyy  linked list.
 * @number: The no insert.
 * Return: 0 If the func fails or pointer to added  node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}
