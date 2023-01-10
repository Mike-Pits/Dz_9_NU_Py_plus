def random_input():
    random_input= (input('Введите элементы через слэш: ')) # Ввод цифр
    l = list(random_input.split(sep='/'))
    l1 = []  # создаем пустой список
    for i in l: # циклом проходим по всем элементам списка, введенных цифр для преобразования их типа даных в int
        l1.append(int(i))
    return set(l1)          # с помощью свойства множества создаем набор уникальных значений


print(list(random_input().symmetric_difference(random_input())))




