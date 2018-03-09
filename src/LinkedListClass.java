/*
 * This class is a practice linked list in Java.
 * Author: Ash Dehghan
 * Date: March 2018
 */
public class LinkedListClass {

	// This class variable head will be the first node
	Node head;
	
	// Internal class, which will define a node
	static class Node{
		int data;
		Node next;
		Node(int d){
			data = d;
			next = null;
		}
	}
	
	public void printList() {
		Node n = head;
		while (n != null) {
			System.out.println(n.data+"\n");
			n = n.next;
		}
	}
	
	
	
}
