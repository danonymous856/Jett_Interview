def reversedList(arr: list):
    start = 0
    end = len(arr)-1

    while start < end:
        swap(arr,start,end)
        start+=1
        end-=1

    return arr


def swap(arr:list,a:int,b:int):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp

a = [1,2,3,4,5,6,7]
print(reversedList(a))