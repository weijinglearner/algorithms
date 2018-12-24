class MaxHeap():
    '''
    2018-12-24
    The root is bigger than its left child and right child.
    '''
    def __init__(self):
        self.array=[]

    def insert(self,num):
        if(not self.array):
            self.array.append(num)
        else:
            self.array.append(num)
            self.siftup(len(self.array)-1)


    def siftup(self,idx):
        if(idx==0):
            return
        parentIdx=(idx - 1) // 2
        if(self.array[parentIdx]<self.array[idx]):
            self.array[parentIdx], self.array[idx] = \
                    self.array[idx], self.array[parentIdx]
            return self.siftup(parentIdx)

    def extractMax(self):
        #swap the head (max) and the last one in self.array, then pop out the max
        if(not self.array):
            raise ValueError("pop out from an empty heap")

        self.array[0],self.array[-1]=self.array[-1],self.array[0]
        max=self.array.pop()
        self.siftdown(0)
        return max


    def siftdown(self,idx):
        '''
        move the current node down
        '''
        if(not self.array or len(self.array)==1):
            return
        left=idx*2+1
        right=idx*2+2
        maxIdx=idx
        if(left<len(self.array) and self.array[maxIdx]<self.array[left]):
            maxIdx=left
        if(right<len(self.array) and self.array[maxIdx]<self.array[right]):
            maxIdx=right

        self.array[idx], self.array[maxIdx] = self.array[maxIdx], self.array[idx]
        #sift down the smaller number recursively
        if(idx!=maxIdx):
            self.siftdown(maxIdx)


    def __str__(self):
        s=""
        for i in range(len(self.array)):
            if(i!=len(self.array)-1):
                s+=str(self.array[i])+" "
            else:
                s+=str(self.array[i])
        return s


heap=MaxHeap()
for i in range(1,10):
    heap.insert(i)
print("After inserting 1,2,3,4,5,6,7,8,9, the array of the heap is {0}.".format(heap))

maxInHeap=heap.extractMax()
print("Pop out from the heap, we'll get the maximum number {0}, "
      "and the array of the heap becomes {1}.".format(maxInHeap,heap))
