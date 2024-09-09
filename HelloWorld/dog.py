class Dog:
    # Constructor 
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    # Method to bark
    def bark(self):
        print("Woof!")

    # Method to display information
    def display_info(self):
        print(f"Name: {self.name}, Breed: {self.breed}")

# Create objects (instances) of the Dog class
my_dog = Dog("Buddy", "Golden Retriever")
your_dog = Dog("Max", "Labrador")

# Call methods on the objects
my_dog.bark()
my_dog.display_info()

your_dog.bark()
your_dog.display_info()