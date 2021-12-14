# python3


def naive_build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                swaps.append((i, j))
                data[i], data[j] = data[j], data[i]
    return swaps

def parent(i):
    return (i-1)//2

def left_child(i):
    return 2*i+1

def right_child(i):
    return 2*i+2

def sift_down(data,i,swaps):  # min-heap sift down
    n = len(data)
    minix = i
    lix = left_child(i)
    if lix <= n-1 and data[lix] < data[minix]:
        minix = lix
    rix = right_child(i)
    if rix <= n-1 and data[rix] < data[minix]:
        minix = rix
    if i != minix:
        swaps.append((i,minix))
        data[i], data[minix] = data[minix], data[i] #swap
        sift_down(data,minix,swaps)

def build_heap(data):
    n = len(data)
    swaps = []
    for i in range(n//2-1, -1, -1):
        sift_down(data,i,swaps)
    return swaps

def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    #swaps = naive_build_heap(data)
    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
