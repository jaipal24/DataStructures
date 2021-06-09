# Given a singly linked list, find the middle of the linked list.
# For example, if the given linked list is 1->2->3->4->5 then the output should be 3.
# If there are even nodes, then there would be two middle nodes, we need to print the second middle element.
# For example, if given linked list is 1->2->3->4->5->6 then the output should be 4.

# node class
class Node:
    # initiating node class object
    def __init__(self, data):
        self.data = data
        self.next = None


# linked list class
class LinkedList:
    # initiating linked list class object
    def __init__(self):
        self.head = None

    # inserting data
    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    # find middle element
    def middle_ele(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data

    def print_list(self):
        if self.head is None:
            print("LinkedList is empty")
            return
        else:
            current = self.head
            while current:
                print(current.data, end="")
                current = current.next


if __name__ == "__main__":
    lt = list(map(int, input("Enter a list of elements:").split()))
    L_list = LinkedList()
    for ele in lt:
        L_list.push(ele)
    L_list.print_list()
    # finding middle element
    print("The middle element is:", L_list.middle_ele())
