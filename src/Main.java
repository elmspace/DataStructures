public class Main {

	public static void main(String[] args) {
		
		LinkedListClass llist = new LinkedListClass();
		
		llist.head = new LinkedListClass.Node(1);
		LinkedListClass.Node second = new LinkedListClass.Node(2);
		LinkedListClass.Node third = new LinkedListClass.Node(3);

		llist.head.next = second;
		second.next = third;
		
		
		llist.printList();
		
	}

}
