class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class slinkedlist:
    def __init__(self):
        self.head=None
 #TRAVERSING THE NODES
    def listprint(self):
        printvalue=self.head
        while printvalue is not None:
            print(printvalue.data)
            printvalue=printvalue.next
list1=slinkedlist()
list1.head=node("100")
list2=node("200")
list3=node("300")
list1.head.next=list2
list2.next=list3
list1.listprint()
