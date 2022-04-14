def bubble_sort(cisla):
    for i in range(len(cisla)-1, 0, -1):
        for j in range(i):
            if cisla[j]>cisla[j+1]:
                cisla[j], cisla[j+1] = cisla[j+1], cisla[j]

cisla = [5, 3, 8, 6, 7, 2]
bubble_sort(cisla)

print(cisla)
