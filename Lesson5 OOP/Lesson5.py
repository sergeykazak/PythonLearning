# В объектно-ориентированном программировании конструктором класса называют метод,
# который автоматически вызывается при создании объектов. Его также можно назвать конструктором объектов класса.
# В Python роль конструктора играет метод __init__()
# Первый его параметр – self – ссылка на сам только что созданный объект.
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname


class Person:
    country = 'USA'  # country is a class variable or attribute. It's a variable that is shared among all instances of the Person class.
    def __init__(self, fname, lname):

        self.fname = fname
        self.lname = lname
        # self.email = f'{fname}'.{lname}@gmail.com # for this row if there will be not @property method email
                                                # then if email is created for the person with specific fname
                                                #and then if fname will be changed email itself will stay unchanged
                                                # until method with @property is added


    @property
    def email(self):
        return f'{self.fname}.{self.lname}@gmail.com'
    def say(self):
        return f'{self.fname} {self.lname} says Hello'


    def learn(self):
        return f'I\'m learning'

    @classmethod
    def change_country(cls, new_country):
        cls.country = new_country
        print(cls.country)

    @staticmethod
    def is_adult(age):
        return age > 18






# cls parameter in a class method (decorated with @classmethod) refers to the class itself.
# It's similar to how self refers to the instance of the class in instance methods.
#
# Here's a brief explanation:
#
# 1. self: Used in instance methods to refer to the instance of the class. It represents the specific instance
# on which the method is being called.
# 2. cls: Used in class methods to refer to the class itself. It represents the class and allows you to
# access class variables and methods.

print(Person.is_adult(15))  # вызов метода cо встроенным декоратором @staticmethod - инстанс создавать не нужно

person1 = Person('John', "Smith")
print(person1.fname)
print(person1.__dict__) # {'fname': 'John', 'lname': 'Smith'}
print(person1.say())
print(person1.country)

person2 = (Person('Andy', 'Jones'))
print(person2.fname)
print(person2.say())

print(person1.email)
person1.fname = 'Mike'
print(person1.fname)
print(person1.email)
print(person1.__dict__)

# Поля/атрибуты класса
# СТАТИЧЕСКИЕ ПОЛЯ (ОНИ ЖЕ ПЕРЕМЕННЫЕ ИЛИ АТРИБУТЫ  КЛАССА) - ЭТО ПЕРЕМЕННЫЕ,
# КОТОРЫЕ ОБЪЯВЛЯЮТСЯ ВНУТРИ ТЕЛА КЛАССА И СОЗДАЮТСЯ ТОГДА, КОГДА СОЗДАЕТСЯ КЛАСС

# ДИНАМИЧЕСКИЕ ПОЛЯ (ПЕРЕМЕННЫЕ ИЛИ АТРИБУТЫ ЭКЗЕМПЛЯРА КЛАССА) – ЭТО ПЕРЕМЕННЫЕ, КОТОРЫЕ СОЗДАЮТСЯ
# НА УРОВНЕ ЭКЗЕМПЛЯРА КЛАССА.

class Developer(Person): #in brackets it's necessary to write class from which current class will be inherited
    def __init__(self, fname, lname, work_language, job_title,salary):
        super().__init__(fname,lname) # to get access to fname and lname on parent class use method super
        self.work_language = work_language
        self._job_title = job_title # with syntax self._job_title we make this field Protected
        self.__salary = salary # field salary is PRIVATE!!!

    def coding(self):
        return f'I\'m coding with {self.work_language}' #escaping '  with \


    def get_salary(self): # this method is needed to control salary field cause it's private
        return self.__salary

    def set_salary(self,new_salary): # this method is needed to control salary field cause it's private
        self.__salary = new_salary


    def learn(self):
        return f'I\'m learning coding'


developer1 = Developer('Alex', 'Smith', 'Java', 'Senior Developer', 100000)
print(developer1)
print(developer1.say())
print(developer1.coding())

print(developer1.get_salary()) # thus we can retrieve salary (private) field
# developer1.__salary = 20000
# print(developer1.get_salary())

developer1.set_salary(230000)
print(developer1.get_salary())

print(developer1._Developer__salary) # way to get access to private field but it's not recommended - ask ChatGPT why

print(developer1._job_title) # way to get access to Protected field job_title

print(developer1.learn())

print(developer1.country) # value USA is inherited from the parent class static field
developer1.change_country('Estonia')
print(developer1.country)





class Junior(Developer):
    def __init__(self,fname, lname, language, job_title,age):
        super().__init__()
        self.age = age

class Tester(Person):
    def __init__(self,fname, lname, framework, job_title):
        super().__init__(fname,lname)
        self.framework = framework
        self.job_title = job_title

    def testing(self):
        return f'I\'m testing with {self.framework}'

tester1 = Tester('Ivan', 'Kazakov', 'selenium', 'Lead QA')
# print(tester1.__dict__)
print(tester1.testing())
print(developer1.country)
print(tester1.country)
tester1.fname = 'Mike'  # можно менять значения полей таким образом
print(tester1.__dict__)



class SDET(Developer, Tester): # inheritance from 2 parents, priority is 1st parent in ()

    def __init__(self, fname,lname,language,job_title,salary, framework):
        Developer.__init__(fname, lname,language,job_title,salary)
        Tester.__init__(framework)

    def build_arch(self):
        return 'I\'m building testing architecture'

arch1 = SDET('Sam', 'Smiths', 'python', 'Architector', 50000, 'Selenium')
print(arch1.__dict__)

# полиморфизм
# ПОЛИМОРФИЗМ - РАЗНОЕ ПОВЕДЕНИЕ ОДНОГО И ТОГО ЖЕ МЕТОДА В РАЗНЫХ КЛАССАХ.


# Абстракция
# АБСТРАКЦИЯ — ЭТО ВЫДЕЛЕНИЕ ОСНОВНЫХ, НАИБОЛЕЕ ЗНАЧИМЫХ ХАРАКТЕРИСТИК ОБЪЕКТА И ИГНОРИРОВАНИЕ ВТОРОСТЕПЕННЫХ.

# Инкапсуляция
# имеет 2 подхода к объяснению
# 1.Инкапсуляция -  ГРУППИРОВКА ЛОГИЧЕСКИ СВЯЗАННЫХ ДАННЫХ И МЕТОДОВ
# 2.Инкапсуляция - МЕХАНИЗМ КОНТРОЛЯ ДОСТУПА К ДАННЫМ
#  2.1 Protected: syntax is the following: self._color = 'grey'  -> values of protected fields can be changed via get/set methods
#  2.2 Public: syntax is: self.color = 'Red'
#  2.3 Private: self.__color = 'Orange' --> _Phone__color

