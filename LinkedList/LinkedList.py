"""
    Thi is a Node class, it is independent of linked list.
    All this is, is a class with two class variables.
    One will hold an object. data is the actual containter.
    Another will hold anothe object, where in this case is another Node object.
    Its like
"""
class Node:
    def __init__(self, data):
        self.data = data;
        self.next = None;


"""
    This is the LinkedList Class, where the constructor is pointing at None by default.
    We can point it to a Node object, with a data and next field.
"""
class LinkedList:
    def __init__(self):
        self.head = None;

    """
        This function will print the list one node at a time
    """
    def printList(self):
        temp = self.head;
        while(temp):
            print temp.data;
            temp = temp.next;


    """
        This function will take in an input data and will create a new Node with that data as
        its data, and will replace the list head with the new node.
        The complexity of this operation is O(1).
    """
    def addInFront(self, data):
        newNode = Node(data);
        newNode.next = self.head;
        self.head = newNode;


    """
        This function will add a new node after a node object.
    """
    def addAfterThisNode(self, data, node):
        newNode = Node(data);
        newNode.next = node.next;
        node.next = newNode;



    """
        This function will create a new node, with data being data input.
        It will then go though the linked list and will add the new node to teh end of the list.
    """
    def addAtTheEnd(self, data):
        newNode = Node(data);
        if (self.head.next == None):
            self.head.next = newNode;
            return;
        temp = self.head;
        while(temp.next):
            temp = temp.next;
        temp.next = newNode;







    # End
