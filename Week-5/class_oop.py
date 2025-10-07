class Gadget:
   
    def __init__(self, name, color):
        # The constructor sets up the initial state of the object.
        self.name = name     
        self.color = color   

    def turn_on(self):
        """A method for turning on the device."""
        print(f"{self.name} is turning on... Hello!")
        
    def show_specs(self):
        """A method to display the gadget's details."""
        print(f"\n--- {self.name} Details ---")
        print(f"Type: Generic Gadget")
        print(f"Color: {self.color}")


class Smartphone(Gadget):
 
    def __init__(self, name, color, apps):
        super().__init__(name, color)
        
        # Add Smartphone-specific attributes.
        self.apps = apps
        
        # Encapsulation: This prevents easy, accidental changes from outside the class.
        self.__battery_level = 75 

    def check_battery(self):
        print(f"Battery Check: {self.__battery_level}% remaining.")

    def charge(self):
        self.__battery_level = 100
        print("Charging complete! Battery is now 100%. 🔋")

    def show_specs(self):
        super().show_specs() # Call the parent's method first for common details
        print(f"Type: Smartphone (Inherited from Gadget)")
        print(f"Installed Apps: {self.apps}")
        self.check_battery() # Also show the battery level

# Create a Smartphone object
my_phone = Smartphone(name="Pixel 8", color="Obsidian Black", apps=["Maps", "Camera", "Music"])

# Demonstrate Inherited method
my_phone.turn_on()

# Demonstrate Encapsulation
my_phone.show_specs()
my_phone.charge()
my_phone.check_battery()

