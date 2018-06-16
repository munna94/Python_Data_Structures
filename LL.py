
#--singly list----
#----define node --------
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

#-- create a class for linked list and initialize the head pointer-----
class LinkedList():
    def __init__(self):
        self.head=None
    #---to insert new node----    
    def insert(self,newNode):
        if self.head is None:
            self.head=newNode
        else:
            cur=self.head
            while(cur.next!=None):
                cur=cur.next
            cur.next=newNode
            
    #---to display---------
    def display(self):
        if self.head==None:
            print("no data")
        else:
            cur=self.head
            while(cur!=None):
                print cur.data
                cur=cur.next
                
     #------to reverse-----------           
    def reverse(self):
        prev=None
        cur=self.head
        while cur!=None:
            nxt=cur.next
            cur.next=prev
            prev=cur
            cur=nxt
        self.head=prev
        
     #--------find length---------   
    def length1(self):
        cur=self.head
        count=0
        while cur!=None:
            count+=1
            cur=cur.next
        return count
    
    #----insert in middle---------
    def insertInMiddle(self,newNode):
        if self.head==None:
            self.head=newNode
            return 
        length=self.length1()
        cur=self.head
        curPoint=0
        while(cur!=None):
            curPoint+=1
            nxt=cur.next
            if(length%2==0):
                if(curPoint==(length/2)):
                    cur.next=newNode
                    newNode.next=nxt
                    break
                else:
                    cur=cur.next
            else:
                if (curPoint==(length+1)/2):
                    cur.next=newNode
                    newNode.next=nxt
                    break
                else:
                    cur=cur.next
                    
    #----insert at specific position-----
    def specificPosition(self,newNode,position):
        if self.head==None:
            self.head=newNode
        elif (position>self.length1()):
            print "bhaiya length is more.., thoda km kr do"
        else:
            cur=self.head
            count=0
            while(cur!=None):
                count+=1
                nxt=cur.next
                if count==position:
                    cur.next=newNode
                    newNode.next=nxt
                    break
                else:
                    cur=cur.next
                    
    
    # ---insert at specific data-------------
    def specificData(self,newNode,dataValue):
        if self.head==None:
            print "no node is available so this is first node"
            self.head=newNode
        else:
            cur=self.head
            while(cur!=None):
                nxt=cur.next
                if(cur.data==dataValue):
                    cur.next=newNode
                    newNode.next=nxt
                    break
                else:
                    cur=cur.next
                    
#---------end of singly linked list---------------    
                    
#---call method----                    
n1=Node(40)
linkd=LinkedList()
linkd.insert(n1)
n2=Node(90)
linkd.insert(n2)

n3=Node(190)
linkd.insert(n3)

n4=Node(290)
linkd.insert(n4)


#---insert in middle----
n5=Node('middle')
linkd.insertInMiddle(n5)


#---insert in middle----
n6=Node('middle1')
linkd.insertInMiddle(n6)

#---insert at position--
n7=Node('munna')
linkd.specificPosition(n7,6)

#insert after specific data-----
n8=Node('1200')
linkd.specificData(n8,'munna')


linkd.display()




# In[67]:


#--circular linked list-----
class CircularNode:
    def __init__(self,data):
        self.data=data
        self.next=None
class CirclularList:
    #--constructure----
    def __init__(self):
        self.head=None
    #--insert data-----
    def insertCircular(self,newNode):
        if self.head==None:
            print "adding first node"
            self.head=newNode
            newNode.next=self.head
        else:
            cur=self.head
            while(cur.next!=self.head):
                cur=cur.next
            cur.next=newNode
            newNode.next=self.head
            
    #----find length--
    def lengthCircular(self):
        if self.head==None:
            print "length is zero"
        else:
            count=1
            cur=self.head
            while(cur.next!=self.head):
                cur=cur.next
                count+=1
            return count
            
            
   #--display-----
    def displayCircular(self):
        if self.head==None:
                print "no node is available to print"
                
        else:
            cur=self.head
            while(cur.next!=self.head):
                print cur.data
                cur=cur.next
            print cur.data
    
    
    
    #----insert at specific position-------
    def insertAtPositionCircular(self,newNode,position):
        if (position==0 or position>self.lengthCircular()):
            print "position is not correct"
        elif self.head==None:
            print "no node is available so first node is inserted"
            self.head=newNode
            newNode.next=self.head
        elif(position==self.lengthCircular()):
            #print "adding to last node"
            cur=self.head
            while(cur.next!=self.head):
                cur=cur.next
            cur.next=newNode
            newNode.next=self.head
            
        else:
            cur=self.head
            count=0
            prev=cur
            while(cur.next!=self.head):
                prev=cur
                cur=cur.next
                count+=1
                if(count==position):
                    break
            prev.next=newNode
            newNode.next=cur
            
    
    
    
    #-----reverse list --------
    def reverseCircular(self):
        if self.head==None:
            print "no node available to reverse"
        else:
            cur1=self.head
            while(cur1.next!=self.head):
                cur1=cur1.next
            prev=cur1
            cur=self.head
            while(cur.next!=self.head):
                cur.next=prev
                prev=cur
                cur=cur.next
            cur.next=prev
            self.head=cur
            #print self.head.data
            
                
                
                
            
        
    
    
    
    
#---call method ---
n1=CircularNode(10)
c1=CirclularList()
c1.insertCircular(n1)

n2=CircularNode(20)
c1.insertCircular(n2)


n3=CircularNode(30)
c1.insertCircular(n3)

c1.displayCircular()
#c1.reverseCircular()   
print ("--------------")                
#c1.reverseCircular()
c1.displayCircular()
                
                
            
    
        
        


# In[8]:


#----doubly linked list ----
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
    
class DoublyLinkedList:
    def __init__(self):
        self.head=None
    #---insert at end (default)-----
    def insertDoubly(self,data):
        newNode=Node(data)
        if self.head==None:
            print "adding first"
            self.head=newNode
        else:
            cur=self.head
            while(cur.next!=None):
                cur=cur.next
            cur.next=newNode
            newNode.prev=cur
            
     #-----insert at begining-----       
    def prepend(self,data):
        newNode=Node(data)
        if self.head is None:
            print "no node is available before adding new ...."
            self.head=newNode
        else:
            cur=self.head
            newNode.next=cur
            cur.prev=newNode
            self.head=newNode
            
    #----find length----        
    def length(self):
        if self.head is None:
            print "length is zero"
        else:
            cur=self.head
            count=1
            while(cur.next!=None):
                count+=1
                cur=cur.next
            return count
              
    #----display ----------            
    def displayDoubly(self):
        if self.head is None:
            print "no node to display"
        else:
            cur =self.head
            while (cur!=None):
                print cur.data
                cur=cur.next
                
    #---insert at specific position-----
    def insertAtSpecific(self,data,position):
        lengthOfList=self.length()
        if self.head is None:
            print ("no existing node. adding new node.... added ")
        elif(position>lengthOfList  or position==0):
            print ("position is not correct")
        else:
            newNode=Node(data)          
            cur=self.head
            count=1
            while(cur!=None):
                if (count==position):
                    nxt=cur.next
                    cur.next=newNode
                    newNode.prev=cur
                    newNode.next=nxt
                    break

                else:
                    if(position==lengthOfList):
                        self.insertDoubly(data)
                        break
                    cur=cur.next
                    count+=1
                    
    
	#---reverse Doubly  -----------
    def reverseDoubly(self):
        if self.head is None:
            print ("there is no node to reverse. sorry...")
        else:
            cur=self.head
            temp=None
            while(cur!=None):
                temp=cur.prev
                cur.prev=cur.next
                cur.next=temp
                cur=cur.prev
                
            #cur.next=cur.prev
            #cur.prev=None
            self.head=temp.prev
                
            
            
            
            
#--call method
dl=DoublyLinkedList()
dl.insertDoubly(10)
dl.insertDoubly(20)
dl.insertDoubly(30)
dl.insertDoubly(40)
dl.prepend('before')
dl.insertDoubly('after')
dl.prepend('before1')
dl.insertDoubly('new added in last')

dl.displayDoubly()
print("--------")
ll=dl.length()
print "length is :",ll
print "-----------"
dl.insertAtSpecific('munna',8)
dl.reverseDoubly()
dl.displayDoubly()

            

