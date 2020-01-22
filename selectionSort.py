def selectionSort(arr):
    for i in range(len(arr)):
        min_number = arr[i]
        swap_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < min_number:
                min_number = arr[j]
                swap_index = j

        arr[i], arr[swap_index] = arr[swap_index], arr[i] 

arr = [8, 3, 5, 4, 6]
selectionSort(arr)
print(arr)
               
   