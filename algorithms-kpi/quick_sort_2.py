def partition(arr, p, r, comparison_count):
    # This function now assumes that the pivot is the last element of the range
    x = arr[r]  # Pivot element
    i = p - 1
    # Increment comparison count for each comparison done in the loop
    comparison_count[0] += (r - p)
    
    for j in range(p, r):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1

def partition_with_first_pivot(arr, p, r, comparison_count):
    # Swap the first element with the last element
    arr[p], arr[r] = arr[r], arr[p]
    # Now call the partition function assuming the last element is the pivot
    return partition(arr, p, r, comparison_count)

def quicksort(arr, p, r, comparison_count):
    if p < r:
        # Use partition_with_first_pivot to swap first and last elements
        q = partition_with_first_pivot(arr, p, r, comparison_count)
        quicksort(arr, p, q - 1, comparison_count)
        quicksort(arr, q + 1, r, comparison_count)

def read_input(filename):
    with open(filename, 'r') as file:
        N = int(file.readline().strip())
        arr = [int(file.readline().strip()) for _ in range(N)]
    return arr

def main():
    filename = '/Users/anastasiiatrofymova/projects/sigma-internship/algorithms-kpi/input__10000.txt'
    arr = read_input(filename)
    
    comparison_count = [0]
    quicksort(arr, 0, len(arr) - 1, comparison_count)
    
    print(f"Total comparisons: {comparison_count[0]}")

main()