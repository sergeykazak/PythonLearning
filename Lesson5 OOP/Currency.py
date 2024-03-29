from __future__ import annotations
from typing import Type

class Currency:

    abbr = 'None'

    rates = {
        "Euro": 1.0,
        "Dollar": 2.0,
        "Pound": 100.00
    }

    def __init__(self,value: float):
        self.value = value

        def get_rate(self,other_cls):
            name = self.__class__.__name__
            rate = other_cls.rates.get(name)
            return rate

        def __gt__(self, other):
            if isinstance(other, Currency):
                other_cls = other.__class__
                rate = self.get_rate(other_cls)
                return self.value > rate * other.value
            else:
                raise ValueError('Unsupported operand type')

        def __lt__(self, other):
            if isinstance(other, Currency):
                other_cls = other.__class__
                rate = self.get_rate(other_cls)
                return self.value < rate * other.value
            else:
                raise ValueError('Unsupported operand type')

        def __eq__(self,other):
            if isinstance(other, Currency):
                other_cls = other.__class__
                rate = self.get_rate(other_cls)
                return self.value == rate * other.value
            else:
                raise ValueError('Unsupported operand type')


        def __add__(self,other): #s a special method that defines the behavior of the + operator when used with
            # instances of a class. This method is called the "addition" or "concatenation" method, and it allows
            # objects of the class to define custom behavior when the + operator is used on them.
            if isinstance(other, Currency):
                other_cls = other.__class__
                rate = self.get_rate(other_cls)
                result = self.value + rate * other.value
                return other_cls(result)
            else:
                raise ValueError('Unsupported operand Type')


    @classmethod # @classmethod is a built-in decorator in Python that allows a method to be called on
    # a class itself rather than on an instance of the class. When you define a method within a class
    # and decorate it with @classmethod, it becomes a class method.
    def course(cls, other_cls: Type[Currency]) -> str:
        name = other_cls.__name__
        rate = cls.rates.get(name)
        return f'{rate} {other_cls.abbr} for 1 {cls.abbr}'

    def to_currency(self, other_cls: Type[Currency]):
        name = other_cls.__name__
        rate = self.rates.get(name)
        converted_value = rate * self.value
        return other_cls(converted_value)

    def __repr__(self):
        return f'{self.value} {self.abbr}'

class Euro(Currency):

    abbr = 'Eur'

    rates = {
        'Euro': 1.0,
        'Dollar': 2.0,
        'Pound': 100.00
    }

    def __init__(self,value: float):
        super().__init__(value)


    def to_currency(self, other_cls: Type[Currency]):
        name = other_cls.__name__
        rate = self .rates.get(name)
        converted_value = rate * self.value
        return other_cls(converted_value)



class Dollar(Currency):

    abbr = 'USD'

    rates = {
        'Dollar': 1.0,
        'Euro': 0.5,
        'Pound': 50.00
    }

    def __init__(self,value: float):
        super().__init__(value)


    def to_currency(self, other_cls: Type[Currency]):
        name = other_cls.__name__
        rate = self .rates.get(name)
        converted_value = rate * self.value
        return other_cls(converted_value)


class Pound(Currency):

    abbr = 'GPB'

    rates = {
        'Pound': 1.0,
        'Dollar': 0.02 ,
        'Euro': 0.01
    }

    def __init__(self,value: float):
        super().__init__(value)


    def to_currency(self, other_cls: Type[Currency]):
        name = other_cls.__name__ # this syntax lets get class name
        rate = self .rates.get(name)
        converted_value = rate * self.value
        return other_cls(converted_value)


dollar = Dollar(100.0)
print(dollar.to_currency(Euro))
print(dollar.to_currency(Pound))
print(dollar.rates)


# @classmethod is a built-in decorator in Python that allows a method to be called on a class itself rather
# than on an instance of the class. When you define a method within a class and decorate it with @classmethod,
# it becomes a class method.

# @staticmethod is another built-in decorator in Python, similar to @classmethod. While @classmethod is used
# to define a method that operates on the class itself, @staticmethod is used to define a method that does
# not have access to the class or instance.

# The main use case for @staticmethod is when you have a method in a class that doesn't depend on the class or
# its instances. It's often used for utility methods or functions that are related to the class but do not need
# access to instance or class variables.


# @property decorator allows you to define a method in a class that can be accessed like an attribute,
# providing a way to encapsulate attribute access and computation. It allows you to define a "getter" method
# for an attribute, which is called when the attribute is accessed.


# @abstractmethod decorator is used to define abstract methods in abstract base classes.
# An abstract method is a method that is declared in the base class but has no implementation.
# It must be overridden by concrete subclasses.