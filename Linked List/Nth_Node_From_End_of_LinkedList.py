# Given a Linked List and a number n,
# write a function that returns the value at the n’th node from the end of the Linked List.

# node class
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

    def length(self):
        count = 0
        if self.head is None:
            return count
        else:
            current = self.head
            while current:
                count += 1
                current = current.next
            return count

    def last_nth_ele(self, pos):
        size = self.length()
        # print(size)
        ind = 0
        current = self.head
        while current:
            if ind == (size-pos):
                return current.data
            ind += 1
            current = current.next
        return "Index out of range"

    def print_list(self):
        if self.head is None:
            print("LinkedList is empty")
            return
        else:
            temp = self.head
            while temp:
                print(temp.data, end=" ")
                temp = temp.next


if __name__ == "__main__":
    lt = list(map(int, input("Enter list of elements:").split()))
    L_list = LinkedList()
    for ele in lt:
        L_list.push(ele)
    print("Linked List:")
    L_list.print_list()
    n = int(input("\nEnter a index from last:"))
    print(L_list.last_nth_ele(n))
