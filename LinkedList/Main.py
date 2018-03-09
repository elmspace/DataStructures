from LinkedList import LinkedList;
from LinkedList import Node;


llist = LinkedList();

FirstNode = Node(1);
SecondNode = Node(2);
ThirdNode = Node(3);

llist.head = FirstNode;

FirstNode.next = SecondNode;
SecondNode.next = ThirdNode;

llist.addInFront("f");

llist.addAtTheEnd("a");


llist.printList();
