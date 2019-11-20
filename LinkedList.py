class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def print_list(self):
        if self.head is None:
            return

        print()
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

        if self.head is None:
            self.head = temp
            return

        temp2 = self.head
        while temp2:
            if temp2.next is None:
                temp2.next = temp
                return
            temp2 = temp2.next

    def delete(self, data):
        if self.head is None:
            return
        temp = self.head
        if temp.data == data:
            self.head = temp.next
            return

        prev = self.head

        while temp:
            if temp.data == data:
                prev.next = temp.next
            prev = temp
            temp = temp.next

    def delete_at_position(self, index):
        if self.head is None:
            return

        temp = self.head
        if index == 0:
            self.head = temp.next
            return

        count = 0
        prev = temp
        while temp:
            if index == count:
                prev.next = temp.next
            prev = temp
            temp = temp.next
            count += 1

    def delete_linked_list(self):
        self.head = None

    def get_length(self):
        count = 0
        if self.head is None:
            return count
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    def search(self, key):
        if self.head is None:
            return False
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False

linked_list = LinkedList()
linked_list.head = Node(1)
second_node = Node(2)
third_node = Node(3)
linked_list.head.next = second_node
second_node.next = third_node
linked_list.print_list()
linked_list.push(4)
linked_list.print_list()
linked_list.push_after(linked_list.get_node(2), 5)
linked_list.print_list()
linked_list.push_end(7)
linked_list.print_list()
linked_list.delete(8)
linked_list.print_list()
linked_list.delete_at_position(0)
linked_list.print_list()
print()
print(linked_list.get_length())
print()
print(linked_list.search(10))
linked_list.delete_linked_list()
linked_list.print_list()

