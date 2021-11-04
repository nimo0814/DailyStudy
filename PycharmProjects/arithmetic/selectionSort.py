def selectionSort(arr):
    for i in range(len(arr)-1):
        #记录最小数的索引
        minIndex=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[minIndex]:
                minIndex=j
        #不是最小数时，将i和和最小数
        if i!=minIndex:
            arr[i],arr[minIndex]=arr[minIndex],arr[i]
    return arr

if __name__=='__main__':
    arr=[5,6,4,8,0,12,9,32,15]
    print(selectionSort(arr))