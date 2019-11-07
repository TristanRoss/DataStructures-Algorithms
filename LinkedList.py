class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def push(self, new_data):
        temp = Node(new_data)
        temp.next = self.head
        self.head = temp

    def push_after(self, prev_node, new_data):
        temp = Node(new_data)
        temp.next = prev_node.next
        prev_node.next = temp

    def get_node(self, data):
        temp = self.head
        while temp:
            if temp.data == data:
                return temp
            temp = temp.next

    def push_end(self, new_data):
        temp = Node(new_data)
        temp2 = self.head

        if temp2 is None:
            temp2.next = temp
            return

        while temp2:
            if temp2.next is None:
                temp2.next = temp
                return
            temp2 = temp2.next


linked_list = LinkedList()
linked_list.head = Node(1)
second_node = Node(2)
third_node = Node(3)
linked_list.head.next = second_node
second_node.next = third_node
linked_list.print_list()
linked_list.push(4)
print()
linked_list.print_list()
print()
linked_list.push_after(linked_list.get_node(2), 5)
linked_list.print_list()
linked_list.push_end(7)
print()
linked_list.print_list()
