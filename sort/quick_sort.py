# Quick Sort
def pivot(arr, start=0, end=None):
    if end is None:
        end = len(arr)+1;
    
    def swap(swapArr,i,j):
        tmp = swapArr[i];
        swapArr[i] = swapArr[j];
        swapArr[j] = tmp;
        
    pivot = arr[start];
    swapIdx = start;
    
    for i in range(start+1, len(arr)):
        if (pivot > arr[i]):
            swapIdx+=1;
            swap(arr, swapIdx, i);
    
    swap(arr, start, swapIdx)
    
    return swapIdx;
    
def quickSort(arr, left = 0, right = None):
    if right is None:
        right = len(arr)-1;
    
    if left < right:
        pivotIndex = pivot(arr, left, right);
        # left
        quickSort(arr,left,pivotIndex-1);
        # right
        quickSort(arr,pivotIndex+1,right)
    return arr;

# Tests
t1 = quickSort([100,-3,2,4,6,9,1,2,5,3,23])
assert t1 == [-3,1,2,2,3,4,5,6,9,23,100]
print(t1)

t2 = quickSort([])
assert t2 == []
print(t2)

t3 = quickSort([100])
assert t3 == [100]
print(t3)

t4 = quickSort([361, 418, 744, 964, 117, 951, 776, 443, 4, 615, 403, 
436, 572, 582, 208, 68, 563, 591, 900, 255, 431, 719, 25, 731, 463, 
890, 397, 278, 715, 991, 300, 91, 426, 881, 268, 698, 351, 524, 457, 
475, 880, 313, 983, 808, 586, 930, 185, 691, 218, 58, 834, 324, 883, 
679, 249, 529, 978, 518, 612, 792, 213, 818, 680, 957, 453, 20, 647, 
654, 79, 282, 565, 863, 711, 635, 877, 344, 189, 526, 713, 630, 905, 
74, 132, 435, 694, 432, 671, 750, 129, 424, 327, 716, 169, 940, 773, 
332, 515, 678, 643, 63])
assert t4 == [4, 20, 25, 58, 63, 68, 74, 79, 91, 117, 129, 132, 169, 
185, 189, 208, 213, 218, 249, 255, 268, 278, 282, 300, 313, 324, 327, 
332, 344, 351, 361, 397, 403, 418, 424, 426, 431, 432, 435, 436, 443, 
453, 457, 463, 475, 515, 518, 524, 526, 529, 563, 565, 572, 582, 586, 
591, 612, 615, 630, 635, 643, 647, 654, 671, 678, 679, 680, 691, 694, 
698, 711, 713, 715, 716, 719, 731, 744, 750, 773, 776, 792, 808, 818, 
834, 863, 877, 880, 881, 883, 890, 900, 905, 930, 940, 951, 957, 964, 
978, 983, 991] 
print(t4)
