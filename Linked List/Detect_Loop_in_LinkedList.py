# Given a linked list, check if the linked list has loop or not.

#node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# linked list class
class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def detect_loop(self):
        s = set()
        current = self.head
        while current:
            if current  in s:
                return True
            s.add(current)
            current = current.next
        return False

    def print_list(self):
        val = []
        temp = self.head
        while temp:
            val.append(str(temp.data))
            temp = temp.next
        return '->'.join(v for v in val)

    def __str__(self):
        return self.print_list()


if __name__ == "__main__":
    L_list = LinkedList()
    L_list.push(1)
    L_list.push(3)
    L_list.push(4)
    L_list.push(5)
    L_list.push(2)
    print("Linked list is:", L_list)
    # creating a loop in the linked list
    L_list.head.next.next.next.next = L_list.head
    if L_list.detect_loop():
        print("Loop Detected")
    else:
        print("No Loop")
