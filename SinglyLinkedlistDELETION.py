class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class slinkedlist:
    def __init__(self):
        self.head=None
    def listprint(self):
        printvalue=self.head
        while printvalue is not None:
            print(printvalue.data)
            printvalue=printvalue.next
    def remove(self,removedata):
       head=self.head
       if head is not None:
           if removedata==head.data:
               self.head=head.next
               head=None
               return
       while head is not None:
           if removedata==head.data:
               break
           prev=head
           head=head.next
       if head==None:
           return
       prev.next=head.next
       head=None
list1=slinkedlist()
list1.head=node("100")
list2=node("200")
list3=node("300")
list1.head.next=list2
list2.next=list3
list1.remove("100")
list1.listprint()

