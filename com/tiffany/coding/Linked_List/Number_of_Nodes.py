# Question: Return the number of nodes in the linked list.

# Examples
# L = null, return 0
# L = 1 -> null, return 1
# L = 1 -> 2 -> null, return 2

# step 1: Node class
class Node():

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data # assign data
        self.next = None # initialize next as None

# step 2: Linked List class contains a Node object
class LinkedList():

    # 2.1: function to initialize head
    def __init__(self):
        self._head = None

    # 2.2: it inserts a new node at the BEGINNING of linked list
    def add(self, new_item):

        # allocate the Node & put it in data
        new_node = Node(new_item)

        # make next of new Node as head
        new_node.next = self._head

        # move the head to point to new node
        self._head = new_node

    # step 3: count how many nodes inside of the linked list
    def length(self):

        # let cur be a pointer, initialize cur
        cur = self._head

        # initialize counting number
        num = 0

        # stop when cur = None, count for each existing node
        while cur != None:
            num += 1
            cur = cur.next
        return num

# Code execution starts here
if __name__ == '__main__':
    p1 = LinkedList()
    p1.add(2)
    p1.add(3)
    p1.add(4)
    print("Count of nodes is : ", p1.length())
