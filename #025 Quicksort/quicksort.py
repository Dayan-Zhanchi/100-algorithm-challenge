def quicksort(a, low, high):
    if low < high:
        p = partition(a, low, high)
        quicksort(a, low, p)
        quicksort(a, p + 1, high)


def partition(a, lo, hi):
    pivot = a[lo + int((hi - lo) / 2)]
    while True:
        while a[lo] < pivot:
            lo += 1
        while a[hi] > pivot:
            hi -= 1

        if lo >= hi:
            return hi

        swap(a, lo, hi)
        lo += 1
        hi -= 1


def swap(a, index1, index2):
    tmp = a[index1]
    a[index1] = a[index2]
    a[index2] = tmp


def main():
    a = [7, 1, 3, 10, 8, 4, 6, 9, 5]
    b = [9, 5, 12, 6, 4, 3, 2, 8]
    quicksort(a, 0, len(a) - 1)
    quicksort(b, 0, len(b) - 1)

if __name__ == '__main__':
    main()
