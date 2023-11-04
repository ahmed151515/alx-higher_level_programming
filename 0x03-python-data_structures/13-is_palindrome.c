#include "lists.h"
/**
 * is_palindrome - is_palindrome
 * head: end linked list
 * Return: 1 or 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *last = *head, *first = *head;

	while (last->next != NULL)
	{
		last = last->next;
	}
	

}
