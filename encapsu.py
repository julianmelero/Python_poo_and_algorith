'''Encapsulation , getters and setters'''

class Person:
    def __init__(self):
        self._name = "No name"
        self._age = 0
    
    def get_name(self):
        return self._name

    def set_age(self,age):
        self._age = age
        print(self._age)
        return self._age

    
    persona = property(get_name, set_age)

Juan = Person()

Juan.persona = 38
print(Juan.persona)


