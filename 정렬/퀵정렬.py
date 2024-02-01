array =[5,7,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
    if start >= end:
        return 
    pivot = start 
    left = start + 1 
    right = end 

    while left <= right:
        # left에서 피벗보다 큰 값 찾기 
        while pivot < array[left] and left <= end:
            left += 1
        # right에서 피벗보다 작은 값 찾기 
        while pivot > array[right] and right >= start:
            right-=1

        # left > right이면 pivot과 right 변경 
        if left > right:
            array[pivot], array[right] = array[right], array[pivot]
        # 아니면 left, right 서로 변경 
        else:
            array[left], array[right] = array[right], array[left]
    # 바뀐 pivot index가 right
    # 왼쪽 오른쪽 분할하여 재귀 
    quick_sort(array, start, right-1)
    quick_sort(array, right, end)

quick_sort(array, 0, len(array)-1)