import time
import csv
import os
import funcs 
import Insertion
import MergeSort
import HybridMerge
import Selection
import Bubble

def CalclulateTime(sortingfunction,array,start,end):
    starttime=time.time()
    sortingfunction(array,start,end)
    endtime=time.time()
    runtime=endtime-starttime
    return runtime

def read_n_from_file():
    given_file = open (file = 'Nvalues.txt', mode = 'r')
    lines = given_file. read ()
    ns = []
    arr = lines.split()
    for s in arr:
        n = int(s)
        ns.append(n)
    return ns

def Write_In_CSV(file, filerow):
    file_exists = os.path.exists(file)
    with open(file, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        if not file_exists:
            writer.writerow(['Value of n', 'InsertionSortTime(sec)', 'MergeSortTime(sec)', 'HybridMergeSortTime(sec)', 'SelectionSortTime(sec)', 'BubbleSortTime(sec)'])
        writer.writerow(filerow)

n_values = read_n_from_file()

for n in n_values:
    arr = funcs.RandomArray(n)

    array_new = arr.copy()
    insertion_sort_time=CalclulateTime(Insertion.InsertionSort,array_new, 0,len(array_new))
    
    array_new = arr.copy() 
    merge_sort_time =CalclulateTime(MergeSort.MergeSort,array_new, 0, len(array_new))
    
    array_new = arr.copy()
    hybrid_merge_sort_time =CalclulateTime(HybridMerge.HybridMergeSort,array_new, 0, len(array_new)-1)
    
    array_new = arr.copy()
    selection_sort_time=CalclulateTime(Selection.SelectionSort,array_new, 0, len(array_new))
    
    array_new = arr.copy()
    bubble_sort_time =CalclulateTime(Bubble.BubbleSort,array_new, 0, len(array_new))

    rowinfile = [n, insertion_sort_time, merge_sort_time, hybrid_merge_sort_time, selection_sort_time, bubble_sort_time]
    Write_In_CSV('RunTime.csv', rowinfile)
    
    print("n={0}, InsertionSortTime={1}s, MergeSortTime={2}s, HybridMergeSortTime={3}s, SelectionSortTime={4}s, BubbleSortTime={5}s".format(
    n, insertion_sort_time, merge_sort_time, hybrid_merge_sort_time, selection_sort_time, bubble_sort_time))