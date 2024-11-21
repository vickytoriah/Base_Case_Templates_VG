# Base_Case_Templates_VG

Repo for class templates and various utility scripts that I commonly use to avoid repetition in coding


<details><summary>Notes to self: Best Practices</summary>
Here are some best practices for using abstract methods in Python:

1. **Use Abstract Base Classes (ABCs) for Interfaces**: Define abstract base classes to create a common interface for related classes. This ensures that all subclasses implement the required methods.

2. **Enforce Method Implementation**: Use the `@abstractmethod` decorator to enforce that certain methods must be implemented in any subclass. This provides a clear contract for developers.

3. **Avoid Instantiating ABCs**: Do not instantiate abstract base classes directly. They are meant to be subclassed, and their abstract methods should be implemented in the subclasses.

4. **Provide Default Implementations Sparingly**: If a method has a common default implementation, provide it in the abstract base class. However, use this sparingly to avoid unnecessary complexity.

5. **Document Abstract Methods**: Clearly document the purpose and expected behavior of abstract methods. This helps other developers understand how to implement them correctly.

6. **Use Abstract Properties**: If you need to enforce the implementation of properties, use the `@property` decorator along with `@abstractmethod`.

7. **Keep Abstract Methods Focused**: Ensure that abstract methods are focused on a single responsibility. This makes them easier to implement and test.

8. **Leverage Multiple Inheritance Carefully**: If using multiple inheritance with abstract base classes, be cautious to avoid the diamond problem and ensure that method resolution order (MRO) is well understood.

Here is an example of using abstract methods and properties in an abstract base class:

```python
```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    @property
    @abstractmethod
    def species(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Bark"

    @property
    def species(self):
        return "Canine"

# Example usage
dog = Dog()
print(dog.make_sound())  # Output: Bark
print(dog.species)       # Output: Canine
```

In this example:
- `Animal` is an abstract base class with an abstract method `make_sound` and an abstract property `species`.
- `Dog` is a concrete class that implements the `make_sound` method and the `species` property.</details>