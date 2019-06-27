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

    def IsExists(self, value):
        """ Search the linked list for a node with the requested value and return the True if it exists otherwise False. """
        if self.head is None:
            return False

        node = self.head
        while node:
            if node.value == value:
                return True
            node = node.next

        return False

def union(llist_1, llist_2):
    """ Union of two given LinkedLists """
    if llist_1.head is None and llist_2.head is None:
        return

    result = LinkedList()
    node1 = llist_1.head
    while node1:
        if not result.IsExists(node1.value):
            result.append(node1.value)
        node1 = node1.next

    node2 = llist_2.head
    while node2:
        if not result.IsExists(node2.value):
            result.append(node2.value)
        node2 = node2.next
    
    return result

def intersection(llist_1, llist_2):
    """ Intersection of two given LinkedLists """
    if llist_1.head is None or llist_2.head is None:
        return

    result = LinkedList()
    node = llist_1.head
    while node:
        if llist_2.IsExists(node.value) and not result.IsExists(node.value):
            result.append(node.value)
        node = node.next

    return (result if result.size() > 0 else None)


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print("------ # Test case 1 Solution ------")
print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print("------ # Test case 2 Solution ------")
print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))

# Test case 3

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = []
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print("------ # Test case 3 Solution ------")
print (union(linked_list_5,linked_list_6))
print (intersection(linked_list_5,linked_list_6))

# Test case 4

linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)

print("------ # Test case 4 Solution ------")
print (union(linked_list_7,linked_list_8))
print (intersection(linked_list_7,linked_list_8))