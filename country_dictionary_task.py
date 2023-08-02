def add_country():
    el = input('Введите страну: ')
    elder[el] = []

def add_city():
    el = input('Введите страну: ')
    if el not in elder:
        print('Такой страны не существует')
    else:
        qalalar = input().split(', ')
        elder[el] = qalalar
        print('Города успешно добавлены')



elder = {}
while True:
    print('1.Добавить страну')
    print('2.Добавить город в страну')
    print('3.Вывести все страны')
    print('4.Вывести все города и страны')
    print('5.Вывести все города определенной страны')
    print('6.Удалить город из страны')
    print('7.Очистить все города из группы')
    print('8.Удалить страну')
    print('0.Выйти')
    command = int(input('Выберите действие: '))
    if command==1:
        add_country()
    elif command==2:
        add_city()
    elif command==3:
        for enter in elder.keys():
            print(enter)
    elif command==4:
        for el, qalalar in elder.items():
            print(el)
            for qala in qalalar:
                print('-',qala)
    elif command==5:
        el = input('Введите страну: ')
        if el in elder:
            for qala in elder[el]:
                print('-',qala)
        else:
            print('Такой страны не существует')
    elif command==6:
        el = input('Введите страну: ')
        if el in elder:
            counter = 0
            for qala in elder[el]:
                counter = counter + 1
                print(counter,qala)
            gorod = int(input('Введите город: '))
            elder[el].pop(gorod-1)
        else:
            print('Такой страны не существует')
    elif command==7:
        el = input('Введите страну: ')
        if el in elder:
            elder[el] = []
            print("Города были очищена")
        else:
            print('Такой страны не существует')
    elif command==8:
        for el in elder:
            print(el)
        delete_el = input('Введите страну: ')
        if delete_el in elder:
            del elder[delete_el]
            print('Страна была удалено')
        else:
            print('Такой страны не существует')
    else:
        print('Вы вышли')
        break


