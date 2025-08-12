from bubble_sort import bubbleSort
from insertion_sort import insertionSort
from selectionsort import selectionSort
from merge_sort import mergeSort
from recursivebubblesort import recursiveBubbleSort
from recursive_selectionsort import recursiveSelectionSort
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

while True:
    try:
        option = int(input("MENU:\n1--SELECTION SORT\n2--BUBBLE SORT\n3--INSERTION SORT\n4--MERGE SORT\n5--RECURSIVE BUBBLE SORT\n6--RECURSIVE SLECTION SORT ,Enter choice (1-6): "))
        break
    except ValueError:
        print("Please enter a valid number (1 to 6). Try again.")


print("-----------------------------------------------\nSORTED LIST ")
if option==1:
    print("Using Selection Sort  :  ",selectionSort(nums))
elif option==2:     
    print("Using Bubble Sort  :  ",bubbleSort(nums))
elif option==3:
    print("Using Insertion  Sort  :  ",insertionSort(nums))
elif option==4:
    print("Using Merge  Sort  :  " ,mergeSort(nums,0,len(nums)-1))
elif option==5:
    print("Using recursive Bubble Sort  :  ",recursiveBubbleSort(nums,len(nums)))
elif option==6:
    print("Using recursive Selection Sort  :  ",recursiveSelectionSort(nums,len(nums)))
else:
    print("invalid choice")

