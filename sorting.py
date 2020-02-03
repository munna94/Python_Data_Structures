
# coding: utf-8

# In[8]:

# bubble sort
def bubbleSort(a):
    for i in range(len(a)-1):
        for j in range(len(a)-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                
    return a
#sortedlist=bubbleSort()
#selection sort

def selectionSort(a):
    for i in range(0,len(a)-1):#because last element will be sorted 
        min=i
        for j in range(i+1,len(a)):
            if a[j]<a[min]:
                min =j
        if min !=i:
            a[i],a[min]=a[min],a[i]
    return a
#insertion sort

def insertionSort(a):
    for i in range(1,len(a)):
        #first is starting,second is end exclude means it will go to -1+1=0,and last is step with -1
        for j in range(i-1,-1,-1):
            if(a[j]>a[j+1]):
                a[j],a[j+1]=a[j+1],a[j]
            else:
                break
    return a


# shifting method of insertion sort
def insertionSort_shifting(a):
    for i in range(1,len(a)):
        temp=a[i]
        for j in range(i-1,-1,-1):
            #print (j)
            if a[j]>temp:
                a[j+1]=a[j]
                j=j-1 #this is required because 
            else:
                break
            
        a[j+1]=temp       
    return a


#---merge sort using recursion--------
def mergesort(listValue):
    if len(listValue)>1:
        mid=len(listValue)//2
        left=listValue[:mid]
        right=listValue[mid:]
        mergesort(left)
        mergesort(right)
        i=j=k=0
        # this is used to merge to sorted listin one big sorted list
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                listValue[k]=left[i]
                i=i+1
            else:
                listValue[k]=right[j]
                j=j+1
            k=k+1
        #when above while loop and condiion fails means either left or right is finished so other will insert as it is 
        while (i<len(left)):
            listValue[k]=left[i]
            i=i+1
            k=k+1
        while(j<len(right)):
            listValue[k]=right[j]
            j=j+1
            k=k+1
    return listValue#this list is pass by rerefence so its changed in original list


#--------quick sort implementation-------------
def partition(l):
    length=len(l)
    pivot=l[length-1]
    left=[]
    right=[]
    for i in range(length-1):
        el=l[i]
        if(el<=pivot):
            left+=[el]
        else:
            right+=[el]
    return (left,pivot,right)
def quick_sort(a):
    if (len(a)<=1):
        return a
    else:
        left,pivot,right=partition(a)
        left_sort=quick_sort(left)
        right_sort=quick_sort(right)
        return left_sort+[pivot]+right_sort
print quick_sort([23,1,-3,450,23,-1,220])




#----------end of quick_sort implementation--------------



