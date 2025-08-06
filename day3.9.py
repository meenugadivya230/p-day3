#binary search :only shorted times use this binary search.it will calculate middle element
list_1 = [1,2,3,4,5,6,7,8,9,10]
target =11
start = 0
end = 9                       #len(list_1)-1
index = -1
while(start<=end):
     midddle = (start+end)//2   #you want to integer value mention //2 or^/2 or int(start+end)/2 
                            # (start+end)/2 this condition gives the any value not only integer
     if list_1[midddle]==target:
        index = midddle
        break    
     elif list_1[midddle]>target:
        end=midddle-1
     elif list_1[midddle]<target:
        satrt=midddle+1
print(index)

