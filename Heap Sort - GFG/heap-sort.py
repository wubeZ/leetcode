#User function Template for python3

class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        
        left = self.left(i)
        right = self.right(i)
        
        largest = i
        
        if left < n and  arr[i] <= arr[left]:
            largest = left
        if right < n and arr[right] >= arr[largest]:
            largest = right
        
        if largest != i:
            arr[largest], arr[i] = arr[i], arr[largest]
            self.heapify(arr, n, largest)
        
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        #step1: find out the middle of the array and heapify the left part
        
        for i in range(n//2-1, -1, -1):
            self.heapify(arr, n, i)
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        #code here
        #step1: build heap -> max_heap or min_heap -> we have to reverse it
        #step2: we have to swap index 0 with index last
        #step2: heapify(array, 0) again
        #step3: removing the last index element
        
        self.buildHeap(arr, n)
        
        dec = 1
        for i in range(n-1, -1, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr, n - dec, 0)
            dec += 1
        
    def left(self, i):
        return 2 * i + 1
    def right(self, i):
        return 2 * i + 2

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Mohit Kumara

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().HeapSort(arr,n)
        print(*arr)

# } Driver Code Ends