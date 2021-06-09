# Given a singly linked list and a key, count the number of occurrences of the given key in the linked list.
# For example, if the given linked list is 1->2->1->2->1->3->1 and the given key is 1, then the output should be 4.

# node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


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

    def count_occurrences(self, ele):
        count = 0
        temp = self.head
        while temp:
            if temp.data == ele:
                count += 1
            temp = temp.next
        return count


if __name__ == "__main__":
    lt = list(map(int, input("Enter elements:").split()))
    L_list = LinkedList()
    for e in lt:
        L_list.push(e)
    val = int(input("Enter element:"))
    print("No of times {0} occurred in linked list is".format(val), L_list.count_occurrences(val))
