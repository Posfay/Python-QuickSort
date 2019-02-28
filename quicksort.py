import random
import datetime

def quicksort(array):
    _quicksort(array, 0, len(array) - 1)

def _quicksort(array, start, stop):
    if stop - start > 0:
        pivot, left, right = array[int((start + stop) / 2)], start, stop
        while left <= right:
            while array[left] < pivot:
                left += 1
            while array[right] > pivot:
                right -= 1
            if left <= right:
                array[left], array[right] = array[right], array[left]
                left += 1
                right -= 1
        _quicksort(array, start, right)
        _quicksort(array, left, stop)

n = 1000
tomb = []

for i in range(n):
    tomb.append(random.randint(0, n))

timeBefore = datetime.datetime.now()

quicksort(tomb)

timeAfter = datetime.datetime.now()

print(timeAfter - timeBefore)

# for i in tomb:
#     print(i)
