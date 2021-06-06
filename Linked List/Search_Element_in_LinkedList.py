# Write a function that searches a given key ‘x’ in a given singly linked list.
# The function should return true if x is present in linked list and false otherwise.
# Node class
class Node:
    # initiating node class object
    def __init__(self, data):
        self.data = data
        self.next = None


# LinkedList class
class LinkedList:
    # initiating linked list class object
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

    # function to search element in linked list in iterative way
    def search_element(self, val):
        if self.head == val:
            return True
        else:
            current = self.head
            while current:
                if current.data == val:
                    return True
                current = current.next
        return False


if __name__ == "__main__":
    L_list = LinkedList()
    # adding some elements into linked list
    L_list.push(1)
    L_list.push(2)
    L_list.push(3)
    L_list.push(4)
    L_list.push(5)
    # searching element in linked list
    if L_list.search_element(4):
        print("Element is found in the linked list")
    else:
        print("Element is not found")
