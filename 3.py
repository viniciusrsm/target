fat = [17, 85, 33, 46, 91, 28, 57, 63, 74, 6, 49, 98, 12, 40, 22, 59, 81, 66, 31, 4, 78, 89, 55, 9, 72, 15, 94, 27, 36, 100, 50]

def menor_valor(lst):
    return sorted(lst)[0]

def maior_valor(lst):
    return sorted(lst)[-1]

def num_dias(lst):
    avg = sum(lst) / len(lst)
    count = 0
    for i in lst:
        count += 1 if i > avg else 0
    return count

print(menor_valor(fat))
print(maior_valor(fat))
print(num_dias(fat))