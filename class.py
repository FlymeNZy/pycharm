#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Person:

    def method(self):
        print("{}'s method".format(self))

    @classmethod
    def class_method(cls):
        print('class = {0.__name__}({0})'.format(cls))
        cls.HEIGHT = 170

    @staticmethod
    def static_method():
        print(Person.HEIGHT)


print('~~~类访问')

print(3, Person.class_method())
print(4, Person.static_method())
print(Person.__dict__)
print('~~~实例访问')
print('tom')
tom = Person()
print(2, tom.method())
print(3, tom.class_method())
print(4, tom.static_method())
print('jerry~~~')
jerry = Person()
print(2, jerry.method())
print(3, jerry.class_method())
print(4, jerry.static_method())
