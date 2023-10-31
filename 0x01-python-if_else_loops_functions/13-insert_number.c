#include "lists.h"
/**
 * insert_node - insert_node
 * head: p
 * number: int
 * Return: node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *c = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
	{
		return (NULL);
	}
	new->n = number;
	while (c != NULL)
	{
		if ((c->next)->n > number)
		{
			new->next = c->next;
			c->next = new;
		}
	}

	return (new);
}
