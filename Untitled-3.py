class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

   
    def insert_at_position(self, data, position):
        new_node = Node(data)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        for i in range(position - 1):
            if temp is None:
                print("Position out of range")
                return
            temp = temp.next

        if temp is None:
            print("Position out of range")
            return

        new_node.next = temp.next
        temp.next = new_node

    
    def delete_first_node(self):
        if self.head is None:
            print("No data element to delete")
            return

        self.head = self.head.next

    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        while temp:
            print(temp.data, end=" -> " if temp.next else "")
            temp = temp.next
        print()



ll = LinkedList()

ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)


print("Original Linked List:")
ll.display()

ll.delete_first_node()

print("After deleting the first node:")
ll.display()



















































































