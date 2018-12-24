import heapq
'''2018-12-24
Use python's heapq to implement a binary max heap.  
'''

class MaxHeapObj(object):
    def __init__(self, val):
        self.val = val

    def __lt__(self, other):
        return self.val > other.val

    def __eq__(self, other):
        return self.val == other.val

    def __str__(self):
        return str(self.val)


class MaxHeap(object):
  def __init__(self):
      self.h = []

  def heappush(self,x):
      heapq.heappush(self.h,MaxHeapObj(x))

  def heappop(self):
      return heapq.heappop(self.h).val

  def __getitem__(self,i):
      return self.h[i].val

  def __str__(self):
      s=""
      for e in self.h:
          s=s+str(e)+" "
      return s


heap=MaxHeap()

for i in range(1,10):
    heap.heappush(i)

print("After inserting 1,2,3,4,5,6,7,8,9, the array of the heap is {0}.".format(heap))

maxInHeap=heap.heappop()
print("Pop out from the heap, we'll get the maximum number {0}, "
      "and the array of the heap becomes {1}.".format(maxInHeap,heap))
