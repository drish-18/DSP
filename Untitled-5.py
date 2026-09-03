class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class CircularDoublyLinkedList:

    def __init__(self):
        self.head = None

    def insert_begin(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
            return

        last = self.head.prev

        new_node.next = self.head
        new_node.prev = last

        last.next = new_node
        self.head.prev = new_node

        self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
            return

        last = self.head.prev

        new_node.next = self.head
        new_node.prev = last

        last.next = new_node
        self.head.prev = new_node

    def insert_position(self, data, position):
        if position <= 0:
            print("Invalid position")
            return

        new_node = Node(data)


        if position == 1:
            self.insert_begin(data)
            return

        if self.head is None:
            print("Invalid position")
            return

        temp = self.head

     
        for i in range(1, position - 1):
            temp = temp.next

            if temp == self.head:
                print("Invalid position")
                return

        new_node.next = temp.next
        new_node.prev = temp

        temp.next.prev = new_node
        temp.next = new_node


    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        while True:        
            print(temp.data, end=" <-> ")
            temp = temp.next

            if temp == self.head:
                break

        print("(back to head)")



cdll = CircularDoublyLinkedList()

cdll.insert_begin(20)
cdll.insert_begin(10)
cdll.insert_end(40)
cdll.insert_end(50)
cdll.insert_position(30, 3)

cdll.display()
 