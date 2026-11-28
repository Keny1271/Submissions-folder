class Dog:
    # Class variable
    animal = "Dog"

    # Constructor with instance variables
    def __init__(self, breed, colour):
        self.breed = breed
        self.colour = colour

    # Method to display dog details
    def display_details(self):
        print(f"Animal: {Dog.animal}")
        print(f"Breed: {self.breed}")
        print(f"Colour: {self.colour}")
        print("-" * 20)


# Creating two different objects for different breeds
dog1 = Dog("Golden Retriever", "Golden")
dog2 = Dog("German Shepherd", "Black and Tan")

# Displaying the details of both dogs
dog1.display_details()
dog2.display_details()
