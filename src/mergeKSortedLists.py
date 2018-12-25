import heapq

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class List(object):
    def __init__(self,array):
        if(array):
            self.head = ListNode(array[0])
            prev=self.head
            cur = None
            for i in range(1,len(array)):
                cur=ListNode(array[i])
                prev.next=cur
                prev=cur
        else:
            self.head = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap=[]
        #init heap, which contains the tuple of head.val and head of each list
        for list in lists:
            if(list):
                heapq.heappush(heap,(list.val,list))

        dummy=ListNode(0)
        tail_new_list=dummy
        #update
        while(heap):
            _,head=heapq.heappop(heap)
            if(head.next):
                heapq.heappush(heap,(head.next.val,head.next))

            tail_new_list.next=head
            tail_new_list=tail_new_list.next
        return dummy.next

def display(head):
    s=""
    cur=head
    while(cur):
        s+=str(cur.val)+" "
        cur=cur.next
    return s


array1=[1,4,5]
list1=List(array1)
print(list1)

array2=[1,3,4]
list2=List(array2)
print(list2)

array3=[2,6]
list3=List(array3)
print(list3)


solution=Solution()
mergedList=solution.mergeKLists([list1.head,list2.head,list3.head])
print(display(mergedList))
