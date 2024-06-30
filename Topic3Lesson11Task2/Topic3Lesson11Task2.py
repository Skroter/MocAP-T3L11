import collections

pets = {1 : {'Кличка': 'Мухтар', 'petsOptins': {'тип': 'Собака', 'возраст': '9 лет.', 'имя хозяина': 'Павел'}}}
petsOptins = {"тип":"str", "возраст":0,"имя хозяина":"str"}
petsKart = {"Кличка":"str","petsOptins":petsOptins}
yearsUpdate = ""
last = 0
command = ""

def create():
    last = collections.deque(pets, maxlen=1)[0] # невозможно применить этот инструмент если изначальный словарь пуст
    print("Введите кличку:")
    pName = input()
    print("Введите тип:")
    type = input()
    print("Введите возраст:")
    years = int(input())
    get_suffix(years)
    print("Введите имя хозяина:")
    pMName = input()
    petsOptins = {"тип":type, "возраст":yearsUpdate,"имя хозяина":pMName}
    petsKart = {"Кличка":pName,"petsOptins":petsOptins}
    pets[last+1] = petsKart
    
def get_suffix(age):
    global yearsUpdate
    if (age == 1) or (age == 21):
        yearsUpdate = str(age) + " год."
    elif (5 > age > 1) or (25 > age > 21) or (35 > age > 31):
        yearsUpdate = str(age) + " года."
    elif (21 > age > 4) or (24 < age < 31) or (age == 0):
        yearsUpdate = str(age) + " лет." 
                
def read():
    print("Карточку какого питомца вы хотите просмотреть, введите ее номер.") 
    print(pets.keys())
    x = int(input())
    x = get_pet(ID=x)
    print("Это", pets[x]['petsOptins']['тип'], "по кличке", '"{}".'.format(pets[x]['Кличка']), 
          "Возраст питомца:",pets[x]['petsOptins']['возраст'],"Имя владельца:",pets[x]['petsOptins']['имя хозяина'])    

def update():
    pets_list()
    print("Введите номер пациента которого вы хотите изменить:")
    x = int(input())
    x = get_pet(ID=x)
    if x in pets.keys():
        print("Введите новые данные питомца:")
        print("Введите кличку:")
        pName = input()
        print("Введите тип:")
        type = input()
        print("Введите возраст:")
        years = int(input())
        get_suffix(years)
        print("Введите имя хозяина:")
        pMName = input()
        petsOptins = {"тип":type, "возраст":yearsUpdate,"имя хозяина":pMName}
        petsKart = {"Кличка":pName,"petsOptins":petsOptins}
        pets[x] = petsKart
    else:
        print("Такого пациента нет")    

def delete():
    pets_list()
    print("Кого удалить введите номер")
    x = int(input())
    x = get_pet(ID=x)
    pets.pop(x)
    if len(pets) == 0:
        petsOptins = {"тип":"", "возраст":0,"имя хозяина":""}
        petsKart = {"Кличка":"","petsOptins":petsOptins}
        pets[0] = petsKart
        

def pets_list(): 
    print("Список пациентов:")
    if len(pets) != 0: 
        for key in pets:
            print("№", key, ":", pets[key])    
    else:
        print ("Словарь пустой") 


def get_pet(ID):
    while ID not in pets.keys():
        if ID not in pets.keys():
            print("такого числа нет, введите заново")
            ID = int(input())
    return ID 


print("Добро пожаловать в ВетКлинику")
while command != 'stop':
    print("Что вы хотите сделать? :")
    print("1 - Создать карточку пациента")
    print("2 - Вывести на экран карточку")
    print("3 - Изменить данные карточки")
    print("4 - Удалить карточку")
    print("stop - выход из программы")
    command = input()
    if command == "1":
        create()
    elif command == "2":
        read()
    elif command == "3":
        update()
    elif command == "4":
        delete()
    elif command == "stop":
        break
print("Программа завершена, до свидания!")