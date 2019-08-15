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
     #INSERTION AT THE BEGINNING
    def atbegin(self,newdata):
        newnode=node(newdata)
        newnode.next=self.head
        self.head=newnode
     #INSERTION AT THE MIDDLE
    def atmiddle(self,middlenode,newdata):
        if middlenode is None:
            print("It is not possible to add in between")
            return
        newnode=node(newdata)
        newnode.next=middlenode.next
        middlenode.next=newnode
     #INSERTION AT THE END
    def atend(self,newdata):
        newnode=node(newdata)
        while list3.next is None:
            list3.next=newnode
list1=slinkedlist()
list1.head=node("100")
list2=node("200")
list3=node("300")
list1.head.next=list2
list2.next=list3
list1.atbegin("50")
list1.atmiddle(list1.head.next,"150")
list1.atend("400")
list1.listprint()
