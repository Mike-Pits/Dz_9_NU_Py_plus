list_number = input('Введите количество элементов: ')

l1 = []

for ln in range(int(list_number)):
    el = int(input(f'Введите элемент {ln+1}: '))
    l1.append(el)

l1.sort()

print(l1)


