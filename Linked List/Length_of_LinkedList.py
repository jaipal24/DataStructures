# Python program to find the length of the linked list
# Node class
class Node:
    # initiating node class object
    def __init__(self, data):
        self.data = data
        self.next = None


# LinkedList class
class LinkedList:
    # initiating LinkedList class object
    def __init__(self):
        self.head = None

    # inserting data into linked list
    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    # function to find length using iteration
    def iter_length(self):
        count = 0
        if self.head is None:
            return count
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    # function to find length using recursion
    def rec_length(self, node):
        if not node:
            return 0
        else:
            return 1 + self.rec_length(node.next)

    def get_rec_length(self):
        return self.rec_length(self.head)


if __name__ == '__main__':
    L_list = LinkedList()
    # adding some elements into linked list
    L_list.push(1)
    L_list.push(2)
    L_list.push(3)
    L_list.push(4)
    L_list.push(5)
    # finding size with iteration
    print(L_list.iter_length())
    # adding some more elements
    L_list.push(6)
    L_list.push(7)
    L_list.push(8)
    # finding length using recursion
    print(L_list.get_rec_length())
