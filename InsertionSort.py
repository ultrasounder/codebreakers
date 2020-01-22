def insertionSort(arr):
    for i in range(len(arr)):
        print(i)
        if i - 1 < 0:
            continue
        for j in range(i - 1, -1, -1):
            print('j=', j)
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print("swap", arr[j], arr[j+1])
                
            else:
                break
arr = [8, 3, 5, 4, 6]
insertionSort(arr)
print(arr)
                
