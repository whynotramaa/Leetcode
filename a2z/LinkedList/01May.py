class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinekdList:
    def __init__(self):
        self.head = None

    def insert_at_start(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_linkedList(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    
    def length(self):
        current = self.head
        x = 0
        while current:
            current = current.next
            x+=1
        print("Total Length = ", x)

ll = LinekdList()
ll.insert_at_start(20)
ll.insert_at_start(30)
ll.insert_at_start(40)


ll.print_linkedList()

class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = DNode(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def insert_at_end(self, data):
        new_node = DNode(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def delete(self, key):
        current = self.head
        if current is None:
            print("List is empty")
            return
        if current.data == key:
            self.head = current.next
            if self.head:
                self.head.prev = None
            return
        while current and current.data != key:
            current = current.next
        if current is None:
            print("Value not found")
            return
        if current.next:
            current.next.prev = current.prev
        if current.prev:
            current.prev.next = current.next

    def search(self, key):
        current = self.head
        position = 0
        while current:
            if current.data == key:
                return position
            current = current.next
            position += 1
        return -1

    def print_forward(self):
        current = self.head
        while current:
            print(current.data, end=" ⇄ ")
            current = current.next
        print("None")

    def print_backward(self):
        current = self.head
        while current.next:
            current = current.next
        while current:
            print(current.data, end=" ⇄ ")
            current = current.prev
        print("None")


dll = DoublyLinkedList()

dll.insert_at_end(10)
dll.insert_at_end(20)
dll.insert_at_end(30)
dll.insert_at_end(40)

dll.print_forward()    # 10 ⇄ 20 ⇄ 30 ⇄ 40 ⇄ None
dll.print_backward()   # 40 ⇄ 30 ⇄ 20 ⇄ 10 ⇄ None

dll.delete(20)
dll.print_forward()    # 10 ⇄ 30 ⇄ 40 ⇄ None

print(dll.search(30))  # 1
print(dll.search(99))  # -1


def reverse(self):
    current = self.head
    while current:
        current.prev, current.next = current.next, current.prev
        new_head = current
        current = current.prev
    
    self.head = new_head