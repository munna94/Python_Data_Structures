#implement stack with push costly means pushing element will be 0(n) inserting to new queue and then finaly copy old
#queue element to new queue
class Stack:
    def __init__(self):
        self.q1=[]
        self.q2=[]
        self.size=0;
    #push implement using queue ALSO CALLED ENQUEUE
    def push(self,ele):
        self.size+=1
        #add new element to q2 at starting so that we can easily pop the latest element . first as stack property
        self.q2.append(ele)
        #and then finally copy the all existing q1 elments to q2 
        while len(self.q1) is not 0:
            poppedQ1=self.q1.pop(0) #pop first element from q1
            #now append to q2
            self.q2.append(poppedQ1)
        #till here q1 is empty and q2 is with latest element first 
        #now we need to swap q2 to q1 so that next time q2 will be empty and q1 will be will all element
        temp=self.q1
        self.q1=self.q2
        self.q2=temp
        
    def pop(self):
        if len(self.q1) is 0:
            print("stack is underflow...")
        else:
	    self.size-=1
            #pop first element from queue and it will be the last pushed element
            ele=self.q1.pop(0)
            return ele
        
    
    def display(self):
        if len(self.q1) is 0:
            print("no element exists...")
        else:
            while (len(self.q1) is not 0):
                #pop first element as queue pop from fron not rear
                ele=self.q1.pop(0)
                print(ele)
                              
stack=Stack()
stack.push(20)
stack.push(20)
stack.push(20)
stack.push(80)
stack.push(180)
#stack.display()
ele=stack.pop()
print("poped element is ",ele)
print("stack left element is in poped order..")
stack.display()
       
