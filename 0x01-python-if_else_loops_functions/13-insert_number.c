#include "lists.h"

/**
 * insert_node - A function that inserts a number in a sorted linked list
 * @head: The head of the list
 * @number: The number to be inserted
 * Return: The address of the new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *new;

	node = *head;
	new = malloc(sizeof(listint_t));
	if (!new)
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
