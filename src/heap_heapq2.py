import heapq
'''2018-12-24
Use python's heapq to implement a binary max heap.  
Since heapq is the min heap, so we need to reimplement 
MaxHeap by multiplying -1 to the item in min heap, and 
multiply -1 as well when using heappop() funciton. 
'''

class MaxHeap(object):
  def __init__(self):
      self.h = []

  def heappush(self,x):
      heapq.heappush(self.h,-x)

  def heappop(self):
      return heapq.heappop(self.h)*(-1)

  def __getitem__(self, i):
      return -1*self.h[i]

  def __str__(self):
      s=""
      for i in range(len(self.h)):
          s=s+str(self[i])+" "
      return s


heap=MaxHeap()

for i in range(1,10):
    heap.heappush(i)

print("After inserting 1,2,3,4,5,6,7,8,9, the array of the heap is {0}.".format(heap))

maxInHeap=heap.heappop()
print("Pop out from the heap, we'll get the maximum number {0}, "
      "and the array of the heap becomes {1}.".format(maxInHeap,heap))
