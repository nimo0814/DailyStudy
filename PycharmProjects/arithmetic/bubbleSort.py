#冒泡排序
def bubbleSort(arr):
    for i in range(1,len(arr)):
        for j in range(0,len(arr)-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

if __name__=='__main__':
    arr=[4,5,13,2,3,6,1,24,56]
    print(bubbleSort(arr))