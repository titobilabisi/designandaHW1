class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = new_node

    def first_index_of(self, x):
        curr_node = self.head
        index = 0
        while curr_node:
            if curr_node.data == x:
                return index
            curr_node = curr_node.next
            index += 1
        return None

    def remove(self, x):
        curr_node = self.head
        prev_node = None
        while curr_node:
            if curr_node.data == x:
                if prev_node:
                    prev_node.next = curr_node.next
                else:
                    self.head = curr_node.next
            else:
                prev_node = curr_node
            curr_node = curr_node.next

    def get_middle(self):
        slow_ptr = self.head
        fast_ptr = self.head
        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        if fast_ptr:
            # Odd number of nodes
            return [slow_ptr.data]
        else:
            # Even number of nodes
            return [slow_ptr.data, slow_ptr.next.data]

    def to_list(self):
        result = []
        curr_node = self.head
        while curr_node:
            result.append(curr_node.data)
            curr_node = curr_node.next
        return result
# Create a linked list
my_list = LinkedList()

# Append elements
my_list.append(1)
my_list.append(7)
my_list.append(5)
my_list.append(4)
my_list.append(2)

# Test first_index_of
print(my_list.first_index_of(5))  # Output: 2

# Test remove
my_list.remove(5)
print(my_list.to_list())  # Output: [1, 7, 4, 2]

# Test get_middle
print(my_list.get_middle())  # Output: [7, 4]

