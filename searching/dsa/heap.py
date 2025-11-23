# for eg lets see this array  arr = [21,17,15,14,9, 12, 13, 8, 5, 1]  considering , a it binary , it children will only be atmost 2.
# the value of item = arr[i] where i is index
# and its left item = 2*i 
# and its right item = 2*i +1
# and its parent = floor(i/2)
 
 
def max_heapify(a, heap_size,i):
    l = 2 *i
    r = 2 *i + 1
    largest = i
     
    if l < heap_size and a[l] > a[i]:
        largest = l
    if r < heap_size and a[r] > a[largest]:
        largest = r
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        max_heapify(a, heap_size,largest)
         
    