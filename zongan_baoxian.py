class Solution:
    def get_pivot_id(self, array, l, r):
        pivot_value=array[r]
        i=l-1
        for j in range(l,r):
            if array[j]>pivot_value:
                i=i+1
                array[i],array[j]=array[j],array[i]
        array[i+1],array[r]=array[r],array[i+1]
        return i+1

    def findKthLargest(self, array: List[int], k: int) -> int:
        # write code here
        l, r = 0, len(array) - 1
        while True:
            pivot_idx = self.get_pivot_id(array[l:r], l, r)
            if pivot_idx==k-1:
                return array[pivot_idx]
            elif pivot_idx<k-1:
                 l=pivot_idx+1
            else:
                 r=pivot_idx-1
i=2

