#Задание 1 хотел расписать алгоритм для тренировки но было лень
prodavec="Здравствуйте вы зашли на наш сайт ,,скупшик228.ru'' напишите характеристики вашей машины"
print(prodavec)
while True:
    class Transport:
        def __init__(self,name,max_speed,milleage):
            self.name=name
            self.max_speed=max_speed
            self.milleage=milleage
        def characteristiky(self):
            print(f"Марка автомобиля:{self.name}\nСкорость:{self.max_speed}\nПробег:{self.milleage}")
            if milleage>20000:
                print("ваш автомобиль непригоден для скупки так как его пробег превышает 20000 или если вы ошиблись нажмите 1 и перезапишите все данные по новой")

    name=input("напишите марку автомобиля")
    max_speed=int(input("напишите максимальную скорость автомобиля"))
    milleage=int(input('напишите его пробег\nпробег не должен превышать 20000км'))

    Autobus=Transport(name,max_speed,milleage)
    Transport.characteristiky(Autobus)
    if name=="BMW":
        print("пошел вон отсюда bmwшник")
        break
    if milleage<20000:
        print("проверьте верно ли вы все ввели все данные напишите 1 ")
    print("если ввели все верно нажмите напишите любое число")
    n = int(input())
    if n == 1:
        print("продолжаем")
    else:break
#Задание 2

class Transport:
    def __init__(self, name, max_speed, milleage):
        self.name = name
        self.max_speed = max_speed
        self.milleage = milleage
    def seating_mesta(self,capacity):
        return ""
class Autobus(Transport):
    capacity = 50
    def seating_mesta(self):
        return f"Вместимость одного автобуса {self.name} {self.capacity}"

a1=Autobus("gag",235,4242)

print(a1.seating_mesta())
