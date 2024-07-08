#day1
class Queue:
    def __init__(self, n):
        self.queue=[]
        self.front= self.rear=0
        self.capacity=n

    def enqueue(self,item):
        if (self.capacity==self.rear):
            print("Queue is full, you cant enqueue")
        else:
            self.queue.append(item)  
            self.rear+=1
            

    def dequeue(self):
        if (self.front == self.rear):
            print("Queue is empty, can't dequeue")
        else:
            x=self.queue.pop(0)
            self.rear-=1

    def display(self):
        if (self.front == self.rear):
            print("Queue is empty, can't display")   
        for i in self.queue:
            print(i, "<--", end='')

    def peek(self):
        if (self.front == self.rear):
            print("Queue is empty, can't peek")  
        else:
           print( "front element is" ,self.queue[self.front]    )

    def size(self):
        print("size of queue is ", len(self.queue))


def menu():
   print("1.Enqueue \n2.Dequeue \n3.Display \n4.Peek \n5.Size of Queue")
   q = Queue(int(input("Enter the capacity of the queue: ")))
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
    elif choice == '5':
        q.size()
    elif choice=='6':
      print("you have exited")
      break    
    else:
        print("invalid")  


menu()   
