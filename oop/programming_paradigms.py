# Programming Paradigms
#######################


# Procedural Programming
# Focus: Step-by-step instructions, variables, and direct execution.
name = "Willie"
age = 6
breed = "Golden Retriever"

# Step-by-step execution
if age < 1:
    status = "puppy"
elif age < 7:
    status = "yang dog"
else:
    status = "senior dog"

# print(f"Name: {name}")
# print(f"Age: {age}")
# print(f"Breed: {breed}")
# print(f"Status: {status}")


# Functional Programming
# Fructions that transforms data and returns results. Avoid side effect.
def create_dog(name, age, breed):
    """Returns a dog dictionary"""
    return {"name": name, "age": age, "breed": breed}

def get_dog_status(age):
    """Always returns same output for same input"""
    if age < 1:
        return "puppy"
    elif age < 7:
        return "yang dog"
    else:
        return "senior dog"

def describe_dog(dog_dict):
    """Transforms data without side effects"""
    status = get_dog_status(dog_dict["age"])
    return f"My dog {dog_dict['name']} is a {dog_dict['breed']} ({status})"

# my_dog = create_dog(name, age, breed)
# description = describe_dog(my_dog)
# print(description)



# OOP - Object Oriented Programming
# Focus: Objects that bundle data (attributes) and behavior (methods).
class Dog:
    def __init__(self, name, age, breed):
        """Constructor - initialize the object"""
        self.name = name
        self.age = age
        self.breed = breed

    def get_status(self):
        """"Method - behavior tied to the object"""
        if self.age < 1:
            return "puppy"
        elif self.age < 7:
            return "young dog"
        else:
            return "senior dog"

    def describe(self):
        status = self.get_status()
        return f"My dog {self.name} is a {self.breed} ({status})"

my_dog = Dog(name, age, breed)
print(my_dog.describe())
