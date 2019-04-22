

class Node:

    def __init__(self,data):
        self.data=data
        self.next=None;


class LinkedList:

    def __init__(self):
        self.head=None;


    def reverse(self):
        prev=None;
        current=self.head;
        while(current is not None):
           next=current.next;
           current.next=prev;
           prev=curr;
           curr=next;

    self.head=prev;


    def push(self,new_data):
        node=Node(new_data);
        node.next=self.head
        self.head=node;


    def printList(self):
        temp=self.head
        while(temp)
            print (temp.data)
            temp=temp.next;





           
    
