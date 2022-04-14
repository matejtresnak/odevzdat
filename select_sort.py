def select_sort(cisla):
    for i in range(0, len(cisla)-1):
        min_value = i
        for j in range(i+1, len(cisla)):
            if cisla[j] < cisla[min_value]:
                min_value = j
        if min_value != i:
            cisla[min_value], cisla[i] = cisla[i], cisla[min_value]
    return cisla

cisla = [6, 8, 7, 2, 3, 0, 1]
select_sort(cisla)
print(cisla)
