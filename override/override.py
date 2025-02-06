class MyClass:
    def __init__(self, value):
        self.value = value

    def __str__(self): # notation to override methods of superclass
        return f"MyClass with value: {self.value}"

    def __repr__(self):
        return f"MyClass({self.value})"

    def __eq__(self, other):
        if isinstance(other, MyClass):
            return self.value == other.value
        return False

    def __add__(self, other):
        if isinstance(other, MyClass):
            return MyClass(self.value + other.value)
        return NotImplemented

# Example usage
obj1 = MyClass(10)
obj2 = MyClass(20)
obj3 = MyClass(10)

print(obj1)  # Output: MyClass with value: 10
print(repr(obj1))  # Output: MyClass(10)
print(obj1 == obj3)  # Output: True
print(obj1 + obj2)  # Output: MyClass with value: 30