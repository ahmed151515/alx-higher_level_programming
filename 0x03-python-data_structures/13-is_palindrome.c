#include "lists.h"
/**
 * is_palindrome - is_palindrome
 * head: end linked list
 * Return: 1 or 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *test = *head;
	size_t count = 0, i;
	int arr[1024];

	while (test != NULL)
	{
		test = test->next;
		count++;
	}
	test = *head;
	for (i = 0; test != NULL; i++)
	{
		arr[i] = test->n;
		test = test->next;
	}
	
	for (count = 0; count <= i; count++)
	{
		if (arr[count] != arr[i])
		{
			return (0);
		}
		i--;
	}
	return (1);
	

}
