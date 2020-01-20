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


#now COSTLYPOPED method implementation 

class PopCostlyStack:
    def __init__(self):
        self.q1=[]
        self.q2=[]
        self.size=0
    def push(self,ele):
        #simply increament count and add to queue
        self.size+=1
        self.q1.append(ele)
        #at last it will be in the format of [1,2,3,4,5]
    def pop(self):
        if len(self.q1) is 0:
            print("stack is underflow...")
            return None
        #now since last element is 5 so stack need to pop 1 first, but from queue 
        #since front is at 1 and rear is at 5 so we can only pop 1
        # for this pop till 4 and copy to q2 and finally pop and return last element which 5 
        else:
            self.size-=1
            while len(self.q1) is not 1:#utill only last index element left
                poppedItem=self.q1.pop(0)#pop first element b/c from queue we only can pop from first index that is front
                self.q2.append(poppedItem)
            #till here q2 will be [1,2,3,4] and q1 will be [5]
            #now pop 5 from q1 that will be the stack pop equivalent
            eleTobereturn=self.q1.pop()
            #now q1 will be [] and q2 will be [1,2,3,4]
            # now we need to swap q1,q2 queue so that next push should be done in q1
            self.q1,self.q2=self.q2,self.q1
            return eleTobereturn
    def display(self):
        if len(self.q1) is 0:
            print("no element exists for display..")
        else:
            while len(self.q1) is not 0:
                ele=self.q1.pop()
                print(ele)
        
stack=PopCostlyStack()
stack.push(12)
stack.push(120)
stack.push(33)
stack.push(45)
stack.push(78)
ele=stack.pop()
print("popped element is ",ele)
print("after popped")
stack.display()
                
                
        
               
