from ZADANIE1.tablica import MonitorowanaTablica

def insertion_sort(array: MonitorowanaTablica, left=0, right=None):
    if right is None:
        right = len(array) - 1

    i = left + 1
    while i <= right:
        j = i
        while j > left and array[j - 1] > array[j]:
            array[j - 1], array[j] = array[j], array[j - 1]
            j -= 1
        i += 1


def bubble_sort(array: MonitorowanaTablica):
    n = len(array)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

                swapped = True

        if not swapped:
            break


def shell_sort(array: MonitorowanaTablica):
    left = 0
    right = len(array) - 1

    h = 1
    while h <= (right - left) // 9:
        h = 3 * h + 1

    while h > 0:
        for i in range(left + h, right + 1):
            j = i

            item = array[i]
            while j >= left + h and item < array[j - h]:
                array[j] = array[j - h]
                j = j - h
            array[j] = item

        h = h // 3




def merge_sort(array: MonitorowanaTablica, left=0, right=None):
    if right is None:
        right = len(array) - 1

    if right - left <= 10:
        for i in range(left + 1, right + 1):
            key = array[i]
            j = i - 1
            while j >= left and array[j] > key:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = key
        return

    if left < right:
        mid = (left + right) // 2
        merge_sort(array, left, mid)
        merge_sort(array, mid + 1, right)

        if array[mid] <= array[mid + 1]:
            return

        merge(array, left, mid, right)

def merge(array: MonitorowanaTablica, left, mid, right):
    left_size = mid - left + 1
    temp = [] 
    
    for i in range(left_size):
        temp.append(array[left + i])
    
    i = 0 
    j = mid + 1
    k = left 
    
    while i < left_size and j <= right:
        if temp[i] <= array[j]:
            array[k] = temp[i]
            i += 1
        else:
            array[k] = array[j]
            j += 1
        k += 1
    
    while i < left_size:
        array[k] = temp[i]
        i += 1
        k += 1

def tim_sort(array: MonitorowanaTablica):
    min_run = 32
    n = len(array)

    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        insertion_sort(array, start, end)

    size = min_run
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(left + size - 1, n - 1)
            right = min(left + 2 * size - 1, n - 1)
            if mid < right:
                temp = []
                i, j = left, mid + 1
                
                while i <= mid and j <= right:
                    if array[i] <= array[j]:
                        temp.append(array[i])
                        i += 1
                    else:
                        temp.append(array[j])
                        j += 1
                
                while i <= mid:
                    temp.append(array[i])
                    i += 1
                
                while j <= right:
                    temp.append(array[j])
                    j += 1
                
                for i, val in enumerate(temp):
                    array[left + i] = val
                    
        size *= 2



def quick_sort(array: MonitorowanaTablica, left=0, right=None):
    if right is None:
        right = len(array) - 1

    if left < right:
        pivot_index = partition(array, left, right)
        quick_sort(array, left, pivot_index - 1)
        quick_sort(array, pivot_index + 1, right)

def partition(array: MonitorowanaTablica, left, right):
    pivot = array[right]
    i = left - 1

    for j in range(left, right):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[right] = array[right], array[i + 1]
    return i + 1






algorytmy = [
    (insertion_sort, "Insertion Sort"),
    (bubble_sort, "Bubble Sort"),
    (shell_sort, "Shell Sort"),
    (merge_sort, "Merge Sort"),
    (quick_sort, "Quick Sort"),
    (tim_sort, "Tim Sort"),
]