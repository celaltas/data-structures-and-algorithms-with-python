

def selection_sort(arr):
    for j in range(len(arr)):
        minimum = arr[j]
        for i in range(j+1, len(arr)):
            if arr[i]<minimum:
                arr[j] = arr[i]
                arr[i] = minimum
                minimum = arr[j]

    return arr









arr = [3,2,13,4,6,5,7,8,1,20]

print(selection_sort(arr))