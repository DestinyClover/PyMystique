def bubbleSort(arr): 
    n = len(arr)  
    for i in range(n-1): 
        for j in range(0, n-i-1): 
              if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
  
arr = eval(input("enter list of numbers"))
bubbleSort(arr) 
print ("Sorted array is:") 
for i in range(len(arr)): 
    print (arr[i],end="   ")
