class Solution:
    def heapify(self, arr, n, i):
        l = 2*i+1
        r = 2*i+2
        largest = i

        if l<n and arr[l] > arr[i]:
            largest = l
        if r<n and arr[r] > arr[largest]:
            largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr,n,largest)

    def buildHeap(self, arr, n):
        for i in range(n,-1,-1):
            self.heapify(arr,n,i)

    def buildHeap(self, arr, n):   # 🔥 duplicate
        return self.buildHeap(arr,n)
