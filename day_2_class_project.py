class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def find_middle(head):
    i = head.next
    j = head
    while i is not None and i.next is not None:
        i =i.next.next
        j = j.next

    return j.value

def revers_list(head):
    i = head
    j = head
    if i.next is None:
        return head

    while j is not None and j.next is not None:
        j = j.next

    while i != j:
        

one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)

one.next = two
two.next = three
three.next = four
four.next = five
five.next = six

