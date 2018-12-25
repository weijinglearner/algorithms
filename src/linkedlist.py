#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class List(object):
    def __init__(self, array):
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

    def __str__(self):
        if(not self.head):
            return "[]"
        else:
            s="["
            cur=self.head
            while(cur):
                s=s+str(cur.val)+" "
                cur=cur.next
            s=s.strip()+"]"
            return s


array1=[1,4,5]
list1=List(array1)
print(list1)
