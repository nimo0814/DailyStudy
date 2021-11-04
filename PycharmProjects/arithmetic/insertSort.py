def insertionSort(arr):
    for i in range(len(arr)):
        preIndex=i-1
        current=arr[i]
        while preIndex>=0 and arr[preIndex]>current:
            arr[preIndex+1]=arr[preIndex]
            preIndex-=1
        arr[preIndex+1]=current
    return arr

if __name__=='__main__':
    arr=[2,1,5,4,11,7,6,14,12,35,23]
    print(insertionSort(arr))