def median_of_three(arr, p, r):
    mid = (p + r) // 2
    first = arr[p]
    middle = arr[mid]
    last = arr[r]

    # Find median of the three elements
    if first < middle:
        if middle < last:
            median = middle
        elif first < last:
            median = last
        else:
            median = first
    else:
        if first < last:
            median = first
        elif middle < last:
            median = last
        else:
            median = middle

    # Return the index of the median element
    if median == arr[p]:
        return p
    elif median == arr[mid]:
        return mid
    else:
        return r

def partition(arr, p, r, comparison_count):
    x = arr[r]  # Pivot element (last element)
    i = p - 1
    # Increment comparison count for each comparison done in the loop
    comparison_count[0] += (r - p)
    
    for j in range(p, r):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1

def partition_with_median_pivot(arr, p, r, comparison_count):
    if r - p + 1 == 2:
        # If there are only two elements, choose the first as the median
        median_index = p
    else:
        median_index = median_of_three(arr, p, r)
    
    # Swap median with the last element
    arr[median_index], arr[r] = arr[r], arr[median_index]
    
    # Call the standard partition procedure
    return partition(arr, p, r, comparison_count)

def quicksort(arr, p, r, comparison_count):
    if p < r:
        q = partition_with_median_pivot(arr, p, r, comparison_count)
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