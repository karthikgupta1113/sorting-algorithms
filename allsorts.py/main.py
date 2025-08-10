from bubble_sort import bubbleSort
from insertion_sort import insertionSort
from selectionsort import selectionSort
# -----INPUT-----
# nums=[1,2,3,5,4]

     #OR
      
# print("----- BY USING THIS CODE YOU CAN SORT ANY LIST ------  ")
# n=int(input("enter size of list  :  "))
# nums=[]
# for i in range(n):
#     nums.append(int(input(f"enter {i+1}th element : ")))

    #OR

nums=list(map(int,input("Enter elements which are separated by spaces  :  ").split()))

#next---->

option=int(input("MENU : \n 1--SELECTION SORT \n 2--BUBBLE SORT \n 3--INSERTION SORT\n CLICK (1,2 or 3) :  "))
if option==1:
    print("SORTED LIST \nthough selection sort  :  ",selectionSort(nums))
elif option==2:     
    print("SORTED LIST \nthough bubble sort  :  ",bubbleSort(nums))
elif option==3:
    print("SORTED LIST \nthough insertion  sort  :  ",insertionSort(nums))
else:
    print("invalid choice")

