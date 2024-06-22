from abc import ABC, abstractmethod
class Person(ABC):
    @abstractmethod
    def complete_work(self):
        pass
class Employee(Person):
    def __init__(self, task):
        self.task = task
        self.completed_task = 0
    def complete_work(self):
        print (f'Сотрудник начал выполнять {self.task}\n')
        self.completed_task += 1
class Worker(Person):
    def __init__(self, work):
        self.work = work
    def complete_work(self):
         print(f'Работник начал {self.work}\n')
class Engineer(Worker):
    def __init__(self, engineer_work):
        self.engineer_work = engineer_work
    def complete_work(self):
        print(f'Инжинер начал {self.engineer_work}\n')
employee = Employee('принести кофе')
employee.complete_work()
print(f'Сотрудник {employee.task} {employee.completed_task} раз\n')
worker = Worker('Водит машину')
worker.complete_work()
engineer = Engineer('Чинит механизм')
engineer.complete_work()

class Detail(ABC):
    @abstractmethod
    def purpose():
        pass
class Yzel(Detail):
    def __init__(self, material):
        self.material = material
    def purpose(self):
        print(f'Узел скрепляет {self.material} кусочка вместе\n')
class Machine(Detail):
    def __init__(self, product):
        self.product = product
    def purpose(self):
        print(f'Делает {self.product}\n')
class Product(Detail):
    def __init__(self, cost):
        self.cost = cost 
    def purpose(self):
        print(f'Стоимость товара {self.cost}\n')
yzel = Yzel('Деревянных')
yzel.purpose()
machine = Machine('Стул')
machine.purpose()
paper_plane = Product('5 тысяч рублей')
paper_plane.purpose()