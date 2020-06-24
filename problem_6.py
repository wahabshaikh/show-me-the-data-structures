class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        out_string += 'None'
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    # Your Solution Here
    union_set = set()

    node = llist_1.head
    while node:
        union_set.add(node.value)
        node = node.next
    
    node = llist_2.head
    while node:
        union_set.add(node.value)
        node = node.next
    
    llist = LinkedList()
    for value in union_set:
        llist.append(value)

    return llist


def intersection(llist_1, llist_2):
    # Your Solution Here
    intersection_set = set()

    set_1 = set()
    node = llist_1.head
    while node:
        set_1.add(node.value)
        node = node.next
    
    set_2 = set()
    node = llist_2.head
    while node:
        set_2.add(node.value)
        node = node.next
    
    for node in set_2:
        if node in set_1:
            intersection_set.add(node)

    llist = LinkedList()
    for value in intersection_set:
        llist.append(value)

    return llist


''' Test case 1 '''

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Expected output:
# 32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21 -> None
# 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 21 -> None


''' Test case 2: Empty Linked Lists '''

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))

# Expected output:
# None
# None


''' Test case 3: Same Linked Lists '''

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [1, 2, 3, 4, 5]
element_2 = [1, 2, 3, 4, 5]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))

# Expected output:
# 1 -> 2 -> 3 -> 4 -> 5 -> None
# 1 -> 2 -> 3 -> 4 -> 5 -> None