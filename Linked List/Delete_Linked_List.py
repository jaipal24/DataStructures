# Python programs to delete the linked list.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # function to insert data into linked list.
    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    # function to print linked list
    def print_list(self):
        if self.head is None:
            print("LinkedList is empty")
            return
        else:
            temp = self.head
            while temp:
                print(temp.data, end=" ")
                temp = temp.next

    # function to delete the linked list
    def delete_linked_list(self):
        current = self.head
        while current:
            prev = current.next
            del current.data
            current = prev
        # In python garbage collection happens so
        # self.head = None
        # will also delete the entire linked list


if __name__ == "__main__":
    # creating a linked list object
    L_list = LinkedList()
    # inserting data into the linked list
    L_list.push(1)
    L_list.push(2)
    L_list.push(3)
    L_list.push(4)
    L_list.push(5)
    print("Linked List elements:")
    L_list.print_list()
    # deleting the linked list
    L_list.delete_linked_list()
