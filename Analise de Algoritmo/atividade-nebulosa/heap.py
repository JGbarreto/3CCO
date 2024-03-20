def left(i):
    """Returns the index of the left child of node i in a heap."""
    return 2 * i + 1

def right(i):
    """Returns the index of the right child of node i in a heap."""
    return 2 * i + 2

def heapify(arr, n, i):
    """Maintains the heap property for a subtree rooted at node i.

    Args:
        arr: The list representing the heap.
        n: The number of elements in the heap.
        i: The index of the node to heapify.
    """
    largest = i  # Initialize largest as root
    l = left(i)   # left = index of left child
    r = right(i)  # right = index of right child

    # Check if left child is larger
    if l < n and arr[l] > arr[largest]:
        largest = l

    # Check if right child is larger
    if r < n and arr[r] > arr[largest]:
        largest = r

    # Swap and continue heapifying if root is not largest
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)

def build_heap(arr, n):
    """Converts a list into a min-heap (root has the minimum element).

    Args:
        arr: The list to be converted into a heap.
        n: The number of elements in the list.
    """
    # Start from (n // 2) - 1 as parent nodes are processed
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    print(arr)

def main():
    # Example usage
    arr = [2, 5, 8 ,13, 21, 1, 3, 34]
    n = len(arr)

    build_heap(arr, n)

    # Print the heap (min-heap in this case)
    print("Min Heap array:", arr)

if __name__ == "__main__":
    main()
