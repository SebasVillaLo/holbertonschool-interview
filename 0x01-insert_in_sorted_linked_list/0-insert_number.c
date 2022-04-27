#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - node to list
 * @head: current node
 * @number: for insert list
 *
 * Return: Always 0.
 */

listint_t *insert_node(listint_t **head, int number)
{
  listint_t *newNode = malloc(sizeof(listint_t));
  listint_t *h = *head;

  if (newNode)
  {
    newNode->n = number;
    newNode->next = NULL;

    if (*head == NULL || (*head)->n >= number)
    {
      newNode->next = *head;
      *head = newNode;
    }
    else
    {
      while (h->next != NULL && h->next->n < number)
      {
        h = h->next;
      }
      newNode->next = h->next;
      h->next = newNode;
    }
    return (newNode);
  }
  return (NULL);
}