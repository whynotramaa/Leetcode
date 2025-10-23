class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtFirst(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new

    def insert(self, data):
        new = Node(data)
        curr = self.head

        if not curr:
            self.head = new
            return

        while curr.next:
            curr = curr.next
        curr.next = new

    def traverse(self):
        curr = self.head
        while curr:
            print(curr.data, end="->")
            curr = curr.next
        print("END")

    def insertAtPos(self, data, pos):
        new = Node(data)

        if pos == 0:
            new.next = self.head
            self.head = new
            return
        curr = self.head

        for _ in range(pos - 1):
            if curr is None:
                raise IndexError("Position is out of bounds")
            curr = curr.next
        new.next = curr.next
        curr.next = new

    def deleteByPos(self, pos):
        curr = self.head
        if pos == 0:
            if curr:
                self.head = curr.next
            return
        for _ in range(pos - 1):
            if curr is None or curr.next is None:
                raise IndexError("Out of bounds")
            curr = curr.next
        curr.next = curr.next.next if curr.next else None

    def reverse(self):
        prev = None
        curr = self.head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            urr = next
        return prev

    def isPalindrome(self,head):
        if not head or not head.next:
            return True

        fast, slow = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        second_half = prev
        first_half = head
        while second_half:
            if first_half.val != second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insertAtHead(self, data):
        new = DNode(data)
        new.next = self.head
        if self.head:
            self.head.prev = new
        self.head = new

    def insertAtTail(self, data):
        new = DNode(data)
        if not self.head:
            self.head = new
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new
        new.prev = curr

    def traversalD(self):
        curr = self.head
        while curr:
            print(curr.data, end="<->")
            curr = curr.next
        print("END")

    def deleteAtPost(self, pos):
        curr = self.head
        if pos == 0:
            if curr:
                self.head = curr.next
                if self.head:
                    self.head.prev = None
            return
        for _ in range(pos):
            if not curr:
                raise IndexError("Pos out of bounds")
            curr = curr.next

        if curr.prev:
            curr.prev.next = curr.next
        if curr.next:
            curr.next.prev = curr.prev




# UNDERSTOOD CIRCULAR LINKED LIST

ll = LinkedList()
ll.insertAtFirst(3)
ll.insert(5)
ll.insert(4)

ll.insertAtPos(98, 3)
ll.insertAtPos(21, 2)

ll.deleteByPos(3)

ll.traverse()
