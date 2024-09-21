lst = [1, 5, 6, 2, 1, 5, 7, 8, -10]

# Bubble Sort Algorithm to sort the list in descending order
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] > lst[j]:  # Change to '<' for descending order
            lst[i], lst[j] = lst[j], lst[i]

print(lst)

lst = [1, 5, 6, 2, 1, 5, 7, 8, -10]
lst_sorted = sorted(lst, reverse=True)  # This uses Timsort, with a typical time complexity of O(n log n)
print(lst_sorted)