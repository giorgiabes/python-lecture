class Dog():
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name.title()} is sitting now.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name.title()} rolled over!")


my_dog = Dog("willie", 6)
print(f"my dog's name is {my_dog.name}.")
print(f"my dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()
