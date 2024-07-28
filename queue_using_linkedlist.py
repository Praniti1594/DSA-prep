class Node:
    def __init__(self, value):
        self.value=value
        self.next=None

class Queue:
    def __init__(self):
        self.front= None
        self.rear=None


    def enqueue(self, item):
        new_node=Node(item)
        if self.front==None and self.rear==None:
            self.front=self.rear=new_node
            # print("Queue is empty")     
        else:
            self.rear.next= new_node
            self.rear= new_node

    def dequeue(self):
        if self.front==None and self.rear==None:
            print("Queue is empty")
        else:
            temp=self.front
            print("Dequeued item is",temp.value) 
            self.front=  self.front.next
        
    def display(self):
        if self.front==None and self.rear==None:
            print("Queue is empty")
        else:
            temp=self.front
            while(temp!=None):
                print(temp.value)
                temp=temp.next

    def peek(self):
        if self.front==None and self.rear==None:
            print("Queue is empty")
        else:
            print(self.front.value)    

def menu():
   print("1.Enqueue \n2.Dequeue \n3.Display \n4.Peek \n5.Exit")
   q = Queue()
   while True:  
    
    choice = input("tell your task")
    if choice == '1':
        item = input("what number to enqueue")
        q.enqueue(item)
    elif choice == '2':
        q.dequeue() 
    elif choice == '3':
        q.display()
    elif choice == '4':
        q.peek()
    elif choice=='5':
      print("you have exited")
      break    
    else:
        print("invalid")  


menu()               
