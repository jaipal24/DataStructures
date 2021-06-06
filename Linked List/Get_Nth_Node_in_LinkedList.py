# Write a GetNth() function that takes a linked list and an integer index
# and returns the data value stored in the node at that index position.

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

    # inserting into linked list
    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    # function to find the nth element in the List
    def get_nth_element(self, ele):
        ind = 0
        current = self.head
        while current:
            if ind == ele:
                return current.data
            current = current.next
            ind += 1
        return "Index out of range"


if __name__ == "__main__":
    lt = list(map(int, input("Enter a list of elements:").split()))
    L_list = LinkedList()
    for val in lt:
        L_list.push(val)
    vl = int(input("Enter node index:"))
    print(L_list.get_nth_element(vl))
