class Wheel:
    colesa = ['None']*4
    def Add(self,x):
        self.colesa[x-1] = 'True'
    def Del(self,x):
        self.colesa[x-1] = 'None'
    
class Dveri:
    doors = ['Закрыто']*4
    def Open(self,x):
        self.doors[x-1] = 'Открыто'
    def Close(self,x):
        self.doors[x-1] = 'Закрыто'



class Fara:
    def TurnOn(self):ЫЫ
        self.farasost = 'ON'
        print('Turned ON')
    def TurnOff(self):
        self.farasost = 'OFF'
        print('Turned OFF')

        
class Machine(Dveri, Wheel, Fara):
 
    def __init__(self, color = None, model = None, price = None, kolvo = None):
        self.farasost = None
        self.color = color
        self.model = model
        self.price = price
        self.kolvo = kolvo
        
    def carinfo(self):
        self.Open(3)
        print(self.doors)

class Interface():
    def __init__(self):
        self.UserInFace()

    def UserInFace(self):
        while True:
            print('1. Добавить машину')
            print('2. Редактировать машину')
            print('3. Посмотреть состояние машины')
            print('4. Список машин')
            print('5. Удаление машин')
            a = input()
            
            #Выбор 1 строки
            if a == '1':
                print('Введите модель')
                massiv.append(Machine(model = input()))
            
            #Выбор 2 строки    
            elif a == '2':
                for i in range(len(massiv)):
                    print(i+1,') ',massiv[i].model, sep = '')
                i = int(input())-1
                print('1. Поменять модель')
                print('2. Поменять цвет')
                print('3. Добавить/удалить колёса')
                print('4. Открыть/закрыть двери')
                print('5. Включить/выключить фары')
                print('6. Изменить стоимость')
                print('0. Назад')
                b = input()

                #Модель
                if b == '1':
                    print('Введите модель')
                    massiv[i].model = input()
                    
                #Цвет    
                if b == '2':
                    print('Введите цвет')
                    massiv[i].color = input()

                #Колёса    
                if b == '3':
                    c = ''
                    while c != '0':
                        print(massiv[i].colesa)
                        print('1. Добавить колесо')
                        print('2. Удалить колесо')
                        print('0. Назад')
                        c = input()
                        if c == '1':
                            print('Введите номер колеса')
                            massiv[i].Add(int(input()))
                        if c == '2':
                            print('Введите номер колеса')
                            massiv[i].Del(int(input()))
                #Двери            
                if b == '4':
                    print('Введите число дверей')
                    c = ''
                    while c != '0':
                        print(massiv[i].doors)
                        print('1. Открыть двери')
                        print('2. Закрыть двери')
                        print('0. Назад')
                        c = input()
                        if c == '1':
                            print('Введите номер двери')
                            massiv[i].Open(int(input()))
                        if c == '2':
                            print('Введите номер колеса')
                            massiv[i].Close(int(input()))

                #Фары
                if b == '5':
                    c = ''
                    while c != '0':
                        print('1. Включить')
                        print('2. Выключить')
                        print('0. Назад')
                        c = input()
                        if c == '1':
                            massiv[i].TurnOn()
                        if c == '2':
                            print('Введите номер колеса')
                            massiv[i].TurnOFF()
                #Стоимость
                if b == '6':
                    print('Введите стоимость')
                    massiv[i].cost = int(input())

                if b == '0':
                    k = Interface()
                    


            #Выбор 3 строки    
            elif a == '3':
                if len(massiv) == 0:
                    print('Нету доступных машин')
                    input()
                else:
                    print('0. Выход')
                    for i in range(len(massiv)):
                        print(i+1,') ',massiv[i].model, sep = '')
                    i = int(input())-1
                    if i == -1:
                        a = Interface()
                    if massiv[i].model != None:
                        print('Модель-', massiv[i].model)
                    if massiv[i].color != None:
                        print('Цвет-', massiv[i].color)
                    if massiv[i].farasost != None:
                        print (massiv[i].farasost)
                    print('Колёса-', massiv[i].colesa)
                    print('Двери -',massiv[i].doors)
                    if massiv[i].price != None:
                        print('Стоимость-', massiv[i].price)
                       
            #Выбор 4 строки
            elif a == '4':
                if len(massiv) == 0:
                    print('Машин нету')
                else:
                    for i in range(len(massiv)):
                        print(i+1,') ',massiv[i].model, sep = '')
                input()
    
            #Выбор 5 строки
            elif a == '5':
                if len(massiv) == 0:
                    print('Нет машин для удаления')
                else:
                    for i in range(len(massiv)):
                        print(i+1,') ',massiv[i].model, sep = '')
                    c = int(input())
                    del massiv[i]

            
massiv = []
a = Interface()
x=int(input())
y=x%2
print(y)
