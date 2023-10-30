#include "lists.h"

/**
 * check_cycle - check_cycle
 * @list: head
 * Return: 1 if true 0 if false
 */
int check_cycle(listint_t *list)
{
	listint_t *test = list;

	if (list == NULL)
	{
		return (0);
	}

	while (test != NULL)
	{
		test = test->next;

		if (test == list)
		{
			return (1);
		}
	}

	return (0);
}
