"""

Jadon Miesle
7/27/24
Final Project
This application functions as an online salad bar, allowing the user
to create their own custom salads from a preselected group of
ingredients, or choose from a selection of premade salads. They
can also add a variety of drinks to their order. They will then
proceed to the checkout where they wil be prompted to enter payment
information.

"""

from breezypythongui import EasyFrame

global totalPrice       # Variable for storing the total cost of the user's order
totalPrice = 0.00
global premadeSaladOrdersDictionary     # Dictionary used for storing the types and quantities of premade salads ordered
premadeSaladOrdersDictionary = {}
global buildingSaladList        # List used to hold ingredients being added to a custom salad
buildingSaladList = []
global builtSaladsList      # List for holding custom salads that have been added to an order
builtSaladsList = []
global listOfIngredients        # List for holding how many of a certain category of ingredients have been added to a salad (for use in determining pricing)
listOfIngredients = []
global priceOfIngredients       # Variable for storing how much to add the the cost of the order based on how many ingredients have been added to a custom salad
priceOfIngredients = 0
global drinkOrdersDictionary     # Dictionary used for storing the types and quantities of drinks ordered
drinkOrdersDictionary = {}

class SaladOrderingApplication(EasyFrame):
    def __init__(self):
        """Constructor creating the window for the saladOrderingApplication class and the buttons to select the items
        to order/proceed to checkout."""
        EasyFrame.__init__(self, 'Salad Ordering Application')      # Create the main window for the Salad Ordering Application
        # Create buttons to add a salad to an order, add a drink to an order, and proceed to checkout (the last of which is disabled
        # by default until any item is added to an order)
        self.addSaladButton = self.addButton(text = 'Add a salad', row = 0, column = 0, command = self.addSalad)
        self.addADrinkButton = self.addButton(text = 'Add a drink', row = 1, column = 0, command = self.addADrink)
        self.checkoutButton = self.addButton(text = 'Proceed to checkout', row = 2, column = 0, command = self.proceedToCheckout, state = 'disabled')
        # Create an exit button
        self.exitButton = self.addButton(text = "Exit", row = 3, column = 0, command = self.exitProgram)
        # Enable the checkout button once any item has been added to the order
        if premadeSaladOrdersDictionary != {} or builtSaladsList != [] or drinkOrdersDictionary != {}:
            self.checkoutButton['state'] = 'active'
    def addSalad(self):
        """Method for adding salads to an order. Gives functionality
        to the "Add a salad" button."""
        SaladOrderingApplication.destroy(self)
        AddSalad().mainloop()
    def addADrink(self):
        """Method for adding drinks to an order. Gives functionality
        to the "Add a drink" button."""
        SaladOrderingApplication.destroy(self)
        AddDrink().mainloop()
    def proceedToCheckout(self):
        """Method for proceeding to checkout. Gives functionality
        to the "Proceed to checkout" button."""
        SaladOrderingApplication.destroy(self)
        ConfirmationScreen().mainloop()
    def exitProgram(self):
        """Method for closing the program. Gives functionality
        to the "Exit" button."""
        exit()

class AddSalad(EasyFrame):
    """This class is used for adding salads to an order. It creates a
    window that gives the user the option of adding a premade salad or
    a custom salad to their order."""
    def __init__(addSaladClass):
        """Constructor creating the window for the addSalad class and the buttons to select which type of salad to add."""
        EasyFrame.__init__(addSaladClass, 'Add a salad')        # Create the window, with the title "Add a salad"
        # Create buttons for adding a premade salad and a custom salad to an order
        addSaladClass.addPremadeSaladButton = addSaladClass.addButton(text = 'Add a premade salad', row = 0, column = 0, command = addSaladClass.addPremadeSalad)
        addSaladClass.addCustomSaladButton = addSaladClass.addButton(text = 'Build your own salad: $6.00+', row = 0, column = 1, command = addSaladClass.addCustomSalad)
        # Create a back button
        addSaladClass.goBack = addSaladClass.addButton(text = "Go back", row = 1, column = 0, command = addSaladClass.goBack)
    def addPremadeSalad(addSaladClass):
        """Method for opening the Add premade salad window"""
        AddSalad.destroy(addSaladClass)     # Close the Add a salad window
        AddPremadeSalad().mainloop()        # Open up the window for adding premade salads to an order
    def addCustomSalad(addSaladClass):
        """Method for opening the Add custom salad window"""
        AddSalad.destroy(addSaladClass)     # Close the Add a salad window
        AddCustomSalad().mainloop()     # Open the window for creating custom salads
    def goBack(addSaladClass):
        """Method for returning to the previous window"""
        AddSalad.destroy(addSaladClass)
        SaladOrderingApplication().mainloop()

class AddPremadeSalad(EasyFrame):
    """This class is used for adding premade salads to an order. It creates a
    window that displays the types and prices of the premade salads available."""
    def __init__(addPremadeSaladClass):
        """Constructor creating the window for the addPremadeSalad class and the buttons to select
        which type of premade salad to add."""
        EasyFrame.__init__(addPremadeSaladClass, 'Add a premade salad')     # Create the window, with the title "Add a salad"
        # Create buttons to add a Caesar salad, taco salad, garden salad, and Greek salad
        addPremadeSaladClass.addCaesarSaladButton = addPremadeSaladClass.addButton(text = 'Add a Caesar salad: $8.00', row = 0, column = 0, 
                                                                                   command = addPremadeSaladClass.addCaesarSalad)
        addPremadeSaladClass.addTacoSaladButton = addPremadeSaladClass.addButton(text = 'Add a taco salad: $7.50', row = 0, column = 1, 
                                                                                 command = addPremadeSaladClass.addTacoSalad)
        addPremadeSaladClass.addGardenSaladButton = addPremadeSaladClass.addButton(text = 'Add a garden salad: $8:50', row = 1, column = 0, 
                                                                                  command = addPremadeSaladClass.addGardenSalad)
        addPremadeSaladClass.addGreekSaladButton = addPremadeSaladClass.addButton(text = 'Add a Greek salad: $7.00', row = 1, column = 1, 
                                                                                  command = addPremadeSaladClass.addGreekSalad)
        # Create a back button
        addPremadeSaladClass.goBack = addPremadeSaladClass.addButton(text = "Go back", row = 2, column = 0, command = addPremadeSaladClass.goBack)
    def addCaesarSalad(addPremadeSaladClass):
        """Method for adding a Caesar salad to the order. Gives functionality
        to the "Add a Caesar salad" button."""
        # Add the cost of a Caesar salad to the total cost of the order
        global totalPrice
        totalPrice += 8.00
        global caesarSaladCount
        # Check to see if the caesarSaladCount variable exists. If it does, increment by one, if not, initialize it to 1
        try:
            caesarSaladCount += 1       # Add 1 to the caesarSaladCount variable (in other words, add a Caesar salad to the order)
        except:
            caesarSaladCount = 1        # Create the variable for counting the number of Caesar salads in the order
        premadeSaladOrdersDictionary['Caesar salad'] = caesarSaladCount
        AddPremadeSalad.destroy(addPremadeSaladClass)       # Close the window for adding premade salads to the order
        SaladOrderingApplication().mainloop()       # Open up the main window again
    def addTacoSalad(addPremadeSaladClass):
        """Method for adding a taco salad to the order. Gives functionality
        to the "Add a taco salad" button."""
        # Add the cost of a taco salad to the total cost of the order
        global totalPrice
        totalPrice += 7.50
        global tacoSaladCount
        # Check to see if the tacoSaladCount variable exists. If it does, increment by one, if not, initialize it to 1
        try:
            tacoSaladCount += 1       # Add 1 to the tacoSaladCount variable (in other words, add a taco salad to the order)
        except:
            tacoSaladCount = 1        # Create the variable for counting the number of taco salads in the order
        premadeSaladOrdersDictionary['taco salad'] = tacoSaladCount
        AddPremadeSalad.destroy(addPremadeSaladClass)       # Close the window for adding premade salads to the order
        SaladOrderingApplication().mainloop()       # Open up the main window again
    def addGardenSalad(addPremadeSaladClass):
        """Method for adding a garden salad to the order. Gives functionality
        to the "Add a garden salad" button."""
        # Add the cost of a garden salad to the total cost of the order
        global totalPrice
        totalPrice += 8.50
        global gardenSaladCount
        # Check to see if the gardenSaladCount variable exists. If it does, increment by one, if not, initialize it to 1
        try:
            gardenSaladCount += 1       # Add 1 to the gardenSaladCount variable (in other words, add a garden salad to the order)
        except:
            gardenSaladCount = 1        # Create the variable for counting the number of garden salads in the order
        premadeSaladOrdersDictionary['garden salad'] = gardenSaladCount
        AddPremadeSalad.destroy(addPremadeSaladClass)       # Close the window for adding premade salads to the order
        SaladOrderingApplication().mainloop()       # Open up the main window again
    def addGreekSalad(addPremadeSaladClass):
        """Method for adding a Greek salad to the order. Gives functionality
        to the "Add a Greek salad" button."""
        # Add the cost of a Greek salad to the total cost of the order
        global totalPrice
        totalPrice += 7.00
        global greekSaladCount
        # Check to see if the greekSaladCount variable exists. If it does, increment by one, if not, initialize it to 1
        try:
            greekSaladCount += 1       # Add 1 to the greekSaladCount variable (in other words, add a Greek salad to the order)
        except:
            greekSaladCount = 1        # Create the variable for counting the number of Greek salads in the order
        premadeSaladOrdersDictionary['Greek salad'] = greekSaladCount
        AddPremadeSalad.destroy(addPremadeSaladClass)       # Close the window for adding premade salads to the order
        SaladOrderingApplication().mainloop()       # Open up the main window again
    def goBack(addPremadeSaladClass):
        """Method for returning to the previous window"""
        AddPremadeSalad.destroy(addPremadeSaladClass)
        AddSalad().mainloop()

class AddCustomSalad(EasyFrame):
    """This class is used for adding custom salads to an order. It creates a
    window that gives the user the options of selecting from various ingredients
    to add to their salad."""
    def __init__(addCustomSaladClass):
        """Constructor creating the window for the addCustomSalad class and the buttons to select
        which ingredients to add."""
        EasyFrame.__init__(addCustomSaladClass, "Select an ingredient type to add to your salad")       # Create the window for adding ingredients to a custom salad
        # Create buttons for adding lettuce, meat, cheese, dressing/sauce, vegetables, and other toppings, and a button
        # for adding the salad to the order
        addCustomSaladClass.addLettuceButton = addCustomSaladClass.addButton(text = 'Add lettuce', row = 0, column = 0,
                                                                             command = addCustomSaladClass.addLettuce)
        addCustomSaladClass.addMeatButton = addCustomSaladClass.addButton(text = 'Add meat', row = 0, column = 1,
                                                                             command = addCustomSaladClass.addMeat)
        addCustomSaladClass.addCheeseButton = addCustomSaladClass.addButton(text = 'Add cheese', row = 1, column = 0,
                                                                             command = addCustomSaladClass.addCheese)
        addCustomSaladClass.addDressingButton = addCustomSaladClass.addButton(text = 'Add a dressing', row = 1, column = 1,
                                                                             command = addCustomSaladClass.addDressing)
        addCustomSaladClass.addVegetableButton = addCustomSaladClass.addButton(text = 'Add vegetables', row = 2, column = 0,
                                                                             command = addCustomSaladClass.addVegetable)
        addCustomSaladClass.addOtherToppingsButton = addCustomSaladClass.addButton(text = 'Add other toppings', row = 2, column = 1,
                                                                             command = addCustomSaladClass.addOtherToppings)
        addCustomSaladClass.confirmSaladOrderButton = addCustomSaladClass.addButton(text = 'Add salad to order', row = 3, column = 1,
                                                                             command = addCustomSaladClass.confirmSaladOrder, state = 'disabled')
        # Add a back button
        addCustomSaladClass.goBack = addCustomSaladClass.addButton(text = "Go back", row = 3, column = 0, command = addCustomSaladClass.goBack)
        global buildingSaladList
        # If there is an ingredient in the buildingSaladList, enable the confirmSaladOrder button
        if buildingSaladList != []:
            addCustomSaladClass.confirmSaladOrderButton['state'] = 'active'
        # For any button, if any of its ingredients are in the salad currently being built, disable it
        if "Romaine lettuce" in buildingSaladList or "Iceberg lettuce" in buildingSaladList or "Shredded lettuce" in buildingSaladList:
            addCustomSaladClass.addLettuceButton['state'] = 'disabled'
        if "Beef" in buildingSaladList or "Chicken" in buildingSaladList or "Turkey" in buildingSaladList or "Diced ham" in buildingSaladList:
            addCustomSaladClass.addMeatButton['state'] = 'disabled'
        if "Cheddar" in buildingSaladList or "Mozzarella" in buildingSaladList or "Colby Jack" in buildingSaladList or "Feta" in buildingSaladList:
            addCustomSaladClass.addCheeseButton['state'] = 'disabled'
        if "Ranch" in buildingSaladList or "Caesar dressing" in buildingSaladList:
            addCustomSaladClass.addDressingButton['state'] = 'disabled'
        if "Carrots" in buildingSaladList or "Green onions" in buildingSaladList or "Onions" in buildingSaladList or "Tomatoes" in buildingSaladList or "Cucumbers" in buildingSaladList or "Cilantro" in buildingSaladList:
            addCustomSaladClass.addVegetableButton['state'] = 'disabled'
        if "Croutons" in buildingSaladList or "Sunflower seeds" in buildingSaladList:
            addCustomSaladClass.addOtherToppingsButton['state'] = 'disabled'
    def addLettuce(addCustomSaladClass):
        """Method for adding lettuce to a custom salad. Gives functionality
        to the "Add lettuce" button"""
        # Close the current window
        AddCustomSalad.destroy(addCustomSaladClass)
        # Open the window for adding lettuce to a salad
        AddLettuce().mainloop()
    def addMeat(addCustomSaladClass):
        """Method for adding meat to a custom salad. Gives functionality
        to the "Add meat" button"""
        # Close the current window
        AddCustomSalad.destroy(addCustomSaladClass)
        # Open the window for adding meats to a salad
        AddMeat().mainloop()
    def addCheese(addCustomSaladClass):
        """Method for adding cheese to a custom salad. Gives functionality
        to the "Add cheese" button"""
        # Close the current window
        AddCustomSalad.destroy(addCustomSaladClass)
        # Open the window for adding cheeses to a salad
        AddCheese().mainloop()
    def addDressing(addCustomSaladClass):
        """Method for adding dressing to a custom salad. Gives functionality
        to the "Add a dressing" button"""
        # Close the current window
        AddCustomSalad.destroy(addCustomSaladClass)
        # Open the window for adding dressings to a salad
        AddDressing().mainloop()
    def addVegetable(addCustomSaladClass):
        """Method for adding vegetables to a custom salad. Gives functionality
        to the "Add vegetables" button"""
        # Close the current window
        AddCustomSalad.destroy(addCustomSaladClass)
        # Open the window for adding vegetables to a salad
        AddVegetable().mainloop()
    def addOtherToppings(addCustomSaladClass):
        """Method for adding other toppings to a custom salad. Gives functionality
        to the "Add other toppings" button"""
        # Close the current window
        AddCustomSalad.destroy(addCustomSaladClass)
        # Open the window for adding other toppings to a salad
        AddOtherTopping().mainloop()
    def confirmSaladOrder(addCustomSaladClass):
        """Method for adding the salad the user just made to an order"""
        # Add the price of a custom salad to the order
        global totalPrice
        totalPrice += 6.00
        global priceOfIngredients
        totalPrice += priceOfIngredients
        # Add a semicolon to the end of the list, to distinguish between individual salads later on
        global buildingSaladList
        buildingSaladList.append(';')
        # Move the contents of buildingSaladList to builtSaladsList for permanent storage
        builtSaladsList.extend(buildingSaladList)
        # Reset buildingSaladList, so it is ready to be reused for the next salad
        buildingSaladList = []
        AddCustomSalad.destroy(addCustomSaladClass)     # Close the window for building your own salad
        SaladOrderingApplication().mainloop()       # Open up the main window again
    def goBack(addCustomSaladClass):
        """Method for returning to the previous window"""
        AddCustomSalad.destroy(addCustomSaladClass)
        AddSalad().mainloop()

class AddLettuce(EasyFrame):
    """Class for adding one type of lettuce to a custom salad"""
    def __init__(addLettuceClass):
        """Constructor for creating the window and buttons for adding lettuce"""
        # Create the window
        EasyFrame.__init__(addLettuceClass, "Add lettuce")
        # Create the radio button group
        addLettuceClass.lettuceGroup = addLettuceClass.addRadiobuttonGroup(row = 0, column = 0, orient = "horizontal", columnspan = 3)
        # Create the default radio button
        defaultRadioButton = addLettuceClass.lettuceGroup.addRadiobutton(text = "Romaine lettuce")
        addLettuceClass.lettuceGroup.setSelectedButton(defaultRadioButton)
        # Create the other two radio buttons
        addLettuceClass.lettuceGroup.addRadiobutton(text = "Iceberg lettuce")
        addLettuceClass.lettuceGroup.addRadiobutton(text = "Shredded lettuce")
        # Create a back button
        addLettuceClass.goBack = addLettuceClass.addButton(text = "Go back", row = 1, column = 0, command = addLettuceClass.goBack)
        # Create a button for adding the lettuce to the salad
        addLettuceClass.confirmLettuceAddition = addLettuceClass.addButton(text = "Confirm", row = 1, column = 2, command = addLettuceClass.confirmLettuceAddition)
    def confirmLettuceAddition(addLettuceClass):
        global buildingSaladList
        buildingSaladList.append(addLettuceClass.lettuceGroup.getSelectedButton() ['text'])
        # Close the add lettuce window
        AddLettuce.destroy(addLettuceClass)
        # Open up the custom salad window again
        AddCustomSalad().mainloop()
    def goBack(addLettuceClass):
        """Method for returning to the previous window"""
        AddLettuce.destroy(addLettuceClass)
        AddCustomSalad().mainloop()

class AddMeat(EasyFrame):
    """Class for adding various meats to a custom salad"""
    def __init__(addMeatClass):
        """Constructor for creating the window and buttons for adding meats"""
        # Create the window
        EasyFrame.__init__(addMeatClass, "Add meat(s)")
        # Add check buttons for the 4 meats
        addMeatClass.addBeefCheckButton = addMeatClass.addCheckbutton(text = "Add beef", row = 0, column = 0)
        addMeatClass.addChickenCheckButton = addMeatClass.addCheckbutton(text = "Add chicken", row = 0, column = 1)
        addMeatClass.addTurkeyCheckButton = addMeatClass.addCheckbutton(text = "Add turkey", row = 1, column = 0)
        addMeatClass.addDicedHamCheckButton = addMeatClass.addCheckbutton(text = "Add diced ham", row = 1, column = 1)
        # Create a back button
        addMeatClass.goBack = addMeatClass.addButton(text = "Go back", row = 2, column = 0, command = addMeatClass.goBack)
        # Add a button for adding the meat to the salad order
        addMeatClass.confirmMeatAddition = addMeatClass.addButton(text = "Confirm", row = 2, column = 1, command = addMeatClass.confirmMeatAddition)
    def confirmMeatAddition(addMeatClass):
        """Event handling method; adds functionality to the four add meat checkboxes"""
        global listOfIngredients
        # If a meat's button is checked, add it to a list of meats to add to the salad
        if addMeatClass.addBeefCheckButton.isChecked():            
            listOfIngredients.append("Beef")
        if addMeatClass.addChickenCheckButton.isChecked():
            listOfIngredients.append("Chicken")
        if addMeatClass.addTurkeyCheckButton.isChecked():   
            listOfIngredients.append("Turkey")
        if addMeatClass.addDicedHamCheckButton.isChecked():           
            listOfIngredients.append("Diced ham")
        numberOfMeats = len(listOfIngredients)      # Determine how many meats have been added to the order, for pricing
        determinePriceIncrease = DetermineNumberOfIngredientAdditions("Meat", numberOfMeats)        # Create an object of the DetermineNumberOfIngredientAdditions class
        determinePriceIncrease.determineIngredientPrice()       # Use the previous object to find how much the price should be increased
        # Add the ingredients to the buildingSaladList
        global buildingSaladList
        buildingSaladList.extend(listOfIngredients)
        # Reset listOfIngredients
        listOfIngredients = []
        # Close the add meat window
        AddMeat.destroy(addMeatClass)
        # Open up the custom salad window again
        AddCustomSalad().mainloop()
    def goBack(addMeatClass):
        """Method for returning to the previous window"""
        AddMeat.destroy(addMeatClass)
        AddCustomSalad().mainloop()

class AddCheese(EasyFrame):
    """Class for adding various cheeses to a custom salad"""
    def __init__(addCheeseClass):
        """Constructor for creating the window and check buttons for adding cheese"""
        # Create the window
        EasyFrame.__init__(addCheeseClass, "Add cheese(s)")
        # Create the check buttons for the cheeses
        addCheeseClass.addCheddarCheckButton = addCheeseClass.addCheckbutton(text = "Add cheddar", row = 0, column = 0)
        addCheeseClass.addMozzarellaCheckButton = addCheeseClass.addCheckbutton(text = "Add mozzarella", row = 0, column = 1)
        addCheeseClass.addColbyJackCheckButton = addCheeseClass.addCheckbutton(text = "Add Colby Jack", row = 1, column = 0)
        addCheeseClass.addFetaCheckButton = addCheeseClass.addCheckbutton(text = "Add feta", row = 1, column = 1)
        # Create a back button
        addCheeseClass.goBack = addCheeseClass.addButton(text = "Go back", row = 2, column = 0, command = addCheeseClass.goBack)
        # Create a button for adding the cheeses to the salad order
        addCheeseClass.confirmCheeseAddition = addCheeseClass.addButton(text = "Confirm", row = 2, column = 1, command = addCheeseClass.confirmCheeseAddition)
    def confirmCheeseAddition(addCheeseClass):
        """Event handling method for the four check buttons and the confirm button"""
        global listOfIngredients
        # If a cheese's button is checked, add it to a list of cheeses to add to the salad
        if addCheeseClass.addCheddarCheckButton.isChecked():
            listOfIngredients.append("Cheddar")
        if addCheeseClass.addMozzarellaCheckButton.isChecked():
            listOfIngredients.append("Mozzarella")
        if addCheeseClass.addColbyJackCheckButton.isChecked():
            listOfIngredients.append("Colby Jack")
        if addCheeseClass.addFetaCheckButton.isChecked():
            listOfIngredients.append("Feta")
        numberOfCheeses = len(listOfIngredients)      # Determine how many cheeses have been added to the order, for pricing
        determinePriceIncrease = DetermineNumberOfIngredientAdditions("Cheese", numberOfCheeses)        # Create an object of the DetermineNumberOfIngredientAdditions class
        determinePriceIncrease.determineIngredientPrice()       # Use the previous object to find how much the price should be increased
        # Add the ingredients to the buildingSaladList
        global buildingSaladList
        buildingSaladList.extend(listOfIngredients)
        # Reset listOfIngredients
        listOfIngredients = []
        # Close the Add cheeses window
        AddCheese.destroy(addCheeseClass)
        # Open up the custom salad window again
        AddCustomSalad().mainloop()
    def goBack(addCheeseClass):
        """Method for returning to the previous window"""
        AddCheese.destroy(addCheeseClass)
        AddCustomSalad().mainloop()

class AddDressing(EasyFrame):
    """Class for adding various dressings to a custom salad"""
    def __init__(addDressingClass):
        """Constructor for creating the window and check buttons for adding dressings"""
        # Create the window
        EasyFrame.__init__(addDressingClass, "Add dressing(s)")
        # Create the check buttons
        addDressingClass.addRanchCheckButton = addDressingClass.addCheckbutton(text = "Add ranch", row = 0, column = 0)
        addDressingClass.addCaesarDressingCheckButton = addDressingClass.addCheckbutton(text = "Add Caesar dressing", row = 0, column = 1)
        # Create a back button
        addDressingClass.goBack = addDressingClass.addButton(text = "Go back", row = 1, column = 0, command = addDressingClass.goBack)
        # Create a button for adding the dressings to the salad order
        addDressingClass.confirmDressingAddition = addDressingClass.addButton(text = "Confirm", row = 1, column = 1, command = addDressingClass.confirmDressingAddition)
    def confirmDressingAddition(addDressingClass):
        """Event handling method for the check buttons and the confirm button"""
        global listOfIngredients
        # If a dressing's button is checked, add it to a list of dressings to add to the salad
        if addDressingClass.addRanchCheckButton.isChecked():
            listOfIngredients.append("Ranch")
        if addDressingClass.addCaesarDressingCheckButton.isChecked():
            listOfIngredients.append("Caesar dressing")
        numberOfDressings = len(listOfIngredients)      # Determine how many dressings have been added to the order, for pricing
        determinePriceIncrease = DetermineNumberOfIngredientAdditions("Dressing", numberOfDressings)       # Create an object of the DetermineNumberOfIngredientAdditions class
        determinePriceIncrease.determineIngredientPrice()       # Use the previous object to find how much the price should be increased
        # Add the ingredients to the buildingSaladList
        global buildingSaladList
        buildingSaladList.extend(listOfIngredients)
        # Reset listOfIngredients
        listOfIngredients = []
        # Close the Add dressings window
        AddDressing.destroy(addDressingClass)
        # Open up the custom salad window again
        AddCustomSalad().mainloop()
    def goBack(addDressingClass):
        """Method for returning to the previous window"""
        AddDressing.destroy(addDressingClass)
        AddCustomSalad().mainloop()

class AddVegetable(EasyFrame):
    """Class for adding various types of vegetables to a custom salad"""
    def __init__(addVegetableClass):
        """Constructor for creating the window and check buttons for adding vegetables"""
        # Create the window
        EasyFrame.__init__(addVegetableClass, "Add vegetable(s)")
        # Create the check buttons
        addVegetableClass.addCarrotCheckButton = addVegetableClass.addCheckbutton(text = "Add carrots", row = 0, column = 0)
        addVegetableClass.addGreenOnionsCheckButton = addVegetableClass.addCheckbutton(text = "Add green onions", row = 0, column = 1)
        addVegetableClass.addOnionsCheckButton = addVegetableClass.addCheckbutton(text = "Add onions", row = 1, column = 0)
        addVegetableClass.addTomatoCheckButton = addVegetableClass.addCheckbutton(text = "Add tomatoes", row = 1, column = 1)
        addVegetableClass.addCucumberCheckButton = addVegetableClass.addCheckbutton(text = "Add cucumbers", row = 2, column = 0)
        addVegetableClass.addCilantroCheckButton = addVegetableClass.addCheckbutton(text = "Add cilantro", row = 2, column = 1)
        # Create a back button
        addVegetableClass.goBack = addVegetableClass.addButton(text = "Go back", row = 3, column = 0, command = addVegetableClass.goBack)
        # Create a button for adding the vegetables to the salad order
        addVegetableClass.confirmVegetableAddition = addVegetableClass.addButton(text = 'Confirm', row = 3, column = 1, command = addVegetableClass.confirmVegetableAddition)
    def confirmVegetableAddition(addVegetableClass):
        """Event handling method for the check buttons and the confirm button"""
        global listOfIngredients
        # If a vegetable's button is checked, add it to a list of vegetables to add to the salad
        if addVegetableClass.addCarrotCheckButton.isChecked():
            listOfIngredients.append("Carrots")
        if addVegetableClass.addGreenOnionsCheckButton.isChecked():
            listOfIngredients.append("Green onions")
        if addVegetableClass.addOnionsCheckButton.isChecked():
            listOfIngredients.append("Onions")
        if addVegetableClass.addTomatoCheckButton.isChecked():
            listOfIngredients.append("Tomatoes")
        if addVegetableClass.addCucumberCheckButton.isChecked():
            listOfIngredients.append("Cucumbers")
        if addVegetableClass.addCilantroCheckButton.isChecked():
            listOfIngredients.append("Cilantro")
        numberOfVegetables = len(listOfIngredients)      # Determine how many vegetables have been added to the order, for pricing
        determinePriceIncrease = DetermineNumberOfIngredientAdditions("Vegetable", numberOfVegetables)       # Create an object of the DetermineNumberOfIngredientAdditions class
        determinePriceIncrease.determineIngredientPrice()       # Use the previous object to find how much the price should be increased
        # Add the ingredients to the buildingSaladList
        global buildingSaladList
        buildingSaladList.extend(listOfIngredients)
        # Reset listOfIngredients
        listOfIngredients = []
        # Close the Add vegetables window
        AddVegetable.destroy(addVegetableClass)
        # Open up the custom salad window again
        AddCustomSalad().mainloop()
    def goBack(addVegetableClass):
        """Method for returning to the previous window"""
        AddVegetable.destroy(addVegetableClass)
        AddCustomSalad().mainloop()

class AddOtherTopping(EasyFrame):
    """Class for adding various other toppings to a custom salad (toppings that don't fit nicely into another category"""
    def __init__(addOtherToppingClass):
        """Constructor for creating the window and check buttons for adding other toppings"""
        # Create the window
        EasyFrame.__init__(addOtherToppingClass, "Add other toppings")
        # Create the check buttons
        addOtherToppingClass.addCroutonCheckButton = addOtherToppingClass.addCheckbutton(text = "Add croutons", row = 0, column = 0)
        addOtherToppingClass.addSunflowerSeedsCheckButton = addOtherToppingClass.addCheckbutton(text = "Add sunflower seeds", row = 0, column = 1)
        # Create a back button
        addOtherToppingClass.goBack = addOtherToppingClass.addButton(text = "Go back", row = 1, column = 0, command = addOtherToppingClass.goBack)
        # Create a button for adding the other toppings to the salad order
        addOtherToppingClass.confirmOtherToppingsAddition = addOtherToppingClass.addButton(text = "Confirm", row = 1, column = 1, command = addOtherToppingClass.confirmOtherToppingsAddition)
    def confirmOtherToppingsAddition(addOtherToppingsClass):
        """Event handling method for the check buttons and the confirm button"""
        global listOfIngredients
        # If a toppings's button is checked, add it to a list of toppings to add to the salad
        if addOtherToppingsClass.addCroutonCheckButton.isChecked():
            listOfIngredients.append("Croutons")
        if addOtherToppingsClass.addSunflowerSeedsCheckButton.isChecked():
            listOfIngredients.append("Sunflower seeds")
        numberOfOtherToppings = len(listOfIngredients)       # Determine how many other toppings have been added to the order, for pricing
        determinePriceIncrease = DetermineNumberOfIngredientAdditions("Other topping", numberOfOtherToppings)       # Create an object of the DetermineNumberOfIngredientAdditions class
        determinePriceIncrease.determineIngredientPrice()       # Use the previous object to find how much the price should be increased
        # Add the ingredients to the buildingSaladList
        global buildingSaladList
        buildingSaladList.extend(listOfIngredients)
        # Reset listOfIngredients
        listOfIngredients = []
        # Close the Add other toppings window
        AddOtherTopping.destroy(addOtherToppingsClass)
        # Open up the custom salad window again
        AddCustomSalad().mainloop()
    def goBack(addOtherToppingClass):
        """Method for returning to the previous window"""
        AddOtherTopping.destroy(addOtherToppingClass)
        AddCustomSalad().mainloop()

class DetermineNumberOfIngredientAdditions(object):
    """Class used to determine how many ingredients of one category have been added to a custom salad and to increase the
    price of the salad accordingly"""
    def __init__(self, ingredient, numberOfIngredients):
        """Constructor creating instance variables for the type of ingredient and number of that ingredient"""
        self.ingredient = ingredient
        self.numberOfIngredients = numberOfIngredients
    def __str__(self):
        """Return the string representation of the class's instance variables"""
        return self.ingredient + " " + str(self.numberOfIngredients)
    def determineIngredientPrice(self):
        """Method for determining how much to add to the price of a salad"""
        # Create a dictionary containing available ingredients
        ingredientPricingDictionary = {"Meat" : 0.75, "Cheese" : 0.50, "Dressing" : 0.35, 
                                       "Vegetable" : 0.40, "Other topping" : 0.30}
        # If the number of ingredients is more than 1, add a certain amount of money (depending on the ingredient, as
        # defined in the previous dictionary) to the order. Otherwise, don't increase the price of the order
        global priceOfIngredients
        if self.numberOfIngredients > 1:
            priceOfIngredients += ingredientPricingDictionary[self.ingredient] * (self.numberOfIngredients - 1)
        else:
            priceOfIngredients += 0

class AddDrink(EasyFrame):
    """This class is used for adding drinks to an order. It creates a window
    that displays the options of drinks and the prices of the drinks, and 
    from which the user can select one of the drinks."""
    def __init__(addDrinkClass):
        """Constructor creating the window for the addDrink class and the buttons to select the drinks."""
        EasyFrame.__init__(addDrinkClass, 'Add a drink')        # Create the window, with the title "Add a drink"
        # Create buttons for adding a water, a lemonade, a pink lemonade, and for opening up another window to select
        # from a list of sodas that the user can order, respectively, and that display the prices of each
        addDrinkClass.addWaterButton = addDrinkClass.addButton(text = 'Add a bottled water: + $0.75', row = 0, column = 0, command = addDrinkClass.addWater)
        addDrinkClass.addLemonadeButton = addDrinkClass.addButton(text = 'Add a lemonade:  + $1.25', row = 0, column = 1, command = addDrinkClass.addLemonade)
        addDrinkClass.addPinkLemonadeButton = addDrinkClass.addButton(text = 'Add a pink lemonade: + $1.25', row = 1, column = 0, command = addDrinkClass.addPinkLemonade)
        addDrinkClass.addSodaButton = addDrinkClass.addButton(text = 'Add a soda: + $1.25', row = 1, column = 1, command = addDrinkClass.addSoda)
        # Create a back button
        addDrinkClass.goBack = addDrinkClass.addButton(text = "Go back", row = 2, column = 0, command = addDrinkClass.goBack)
    def addWater(addDrinkClass):
        """Method for adding a water to the order. Gives functionality
        to the "Add a bottled water" button."""
        # Add the cost of a water to the total cost of the order
        global totalPrice
        totalPrice += 0.75
        global waterCount
        # Check to see if the waterCount variable exists, and, if not, initialize it to 1
        try:
            waterCount += 1     # Check for the waterCount variable, and increment it by one if it exists
        except:
            waterCount = 1     # Create the waterCount variable, which stores the total amount of bottled waters the user has ordered
        # Either add water to the dictionary for storing the user's drink orders, or update the total number of waters ordered
        drinkOrdersDictionary['water'] = waterCount         
        AddDrink.destroy(addDrinkClass)     # Remove the window for adding drinks to the order
        SaladOrderingApplication().mainloop()       # Open up the main window again
    def addLemonade(addDrinkClass):
        """Method for adding a lemonade to the order. Gives functionality
        to the "Add a lemonade" button."""
        # Add the cost of a lemonade to the total cost of the order
        global totalPrice
        totalPrice += 1.25
        global lemonadeCount
        # Check to see if the lemonadeCount variable exists, and, if not, initialize it to 1
        try:
            lemonadeCount += 1     # Check for the lemonadeCount variable, and increment it by one if it exists
        except:
            lemonadeCount = 1      # Create the lemonadeCount variable, which stores the total amount of lemonades the user has ordered
        # Either add lemonade to the dictionary for storing the user's drink orders, or update the total number of lemonades ordered
        drinkOrdersDictionary['lemonade'] = lemonadeCount
        AddDrink.destroy(addDrinkClass)     # Remove the window for adding drinks to the order
        SaladOrderingApplication().mainloop()       # Open up the main window again
    def addPinkLemonade(addDrinkClass):
        """Method for adding a pink lemonade to the order. Gives functionality
        to the "Add a pink lemonade" button."""
        # Add the cost of a pink lemonade to the total cost of the order
        global totalPrice
        totalPrice += 1.25
        global pinkLemonadeCount
        # Check to see if the pinkLemonadeCount variable exists, and, if not, initialize it to 1
        try:
            pinkLemonadeCount += 1     # Check for the pinkLemonadeCount variable, and increment it by one if it exists
        except:
            pinkLemonadeCount = 1      # Create the pinkLemonadeCount variable, which stores the total amount of pink lemonades the user has ordered
        # Either add pink lemonade to the dictionary for storing the user's drink orders, or update the total number of pink lemonades ordered
        drinkOrdersDictionary['pink lemonade'] = pinkLemonadeCount
        AddDrink.destroy(addDrinkClass)     # Remove the window for adding drinks to the order
        SaladOrderingApplication().mainloop()       # Open up the main window again
    def addSoda(addDrinkClass):
        AddDrink.destroy(addDrinkClass)     # Remove the window for adding drinks to the order
        AddSoda().mainloop()        # Open up the window for adding a soda to the order
    def goBack(addDrinkClass):
        """Method for returning to the previous window"""
        AddDrink.destroy(addDrinkClass)
        SaladOrderingApplication().mainloop()

class AddSoda(EasyFrame):
    """This class creates a window that allows the user to select
    one of many sodas to add to their order."""
    def __init__(addSodaClass):
        """Constructor creating the window for the addSoda class and the buttons to select the sodas."""
        EasyFrame.__init__(addSodaClass, 'Add a soda')        # Create the window, with the title "Add a soda"
        # Create buttons for adding a Pepsi, Coca-Cola, root beer, Sprite, and Dr. Pepper to an order
        addSodaClass.addPepsiButton = addSodaClass.addButton(text = 'Add a Pepsi', row = 0, column = 0, command = addSodaClass.addPepsi)
        addSodaClass.addCocaColaButton = addSodaClass.addButton(text = 'Add a Coca-Cola', row = 0, column = 1, command = addSodaClass.addCocaCola)
        addSodaClass.addRootBeerButton = addSodaClass.addButton(text = 'Add a Root Beer', row = 1, column = 0, command = addSodaClass.addRootBeer)
        addSodaClass.addSpriteButton = addSodaClass.addButton(text = 'Add a Sprite', row = 1, column = 1, command = addSodaClass.addSprite)
        addSodaClass.addDrPepperButton = addSodaClass.addButton(text = 'Add a Dr Pepper', row = 2, column = 1, command = addSodaClass.addDrPepper)
        addSodaClass.goBack = addSodaClass.addButton(text = "Go back", row = 2, column = 0, command = addSodaClass.goBack)
    def addPepsi(addSodaClass):
        """Method for adding a Pepsi to the order. Gives functionality
        to the "Add a Pepsi" button."""
        # Add the cost of a Pepsi to the total cost of the order
        global totalPrice
        totalPrice += 1.25
        global pepsiCount
        # Check to see if the pepsiCount variable exists, and, if not, initialize it to 1
        try:
            pepsiCount += 1     # Check for the pepsiCount variable, and increment it by one if it exists
        except:
            pepsiCount = 1      # Create the pepsiCount variable, which stores the total amount of Pepsi's the user has ordered
        # Either add Pepsi to the dictionary for storing the user's drink orders, or update the total number of Pepsi's ordered
        drinkOrdersDictionary['Pepsi'] = pepsiCount
        AddSoda.destroy(addSodaClass)       # Remove the window for adding sodas to the order
        SaladOrderingApplication().mainloop()       # Open up the main window again
    def addCocaCola(addSodaClass):
        """Method for adding a Coca-Cola to the order. Gives functionality
        to the "Add a Coca-Cola" button."""
        # Add the cost of a Coca-Cola to the total cost of the order
        global totalPrice
        totalPrice += 1.25
        global cocaColaCount
        # Check to see if the cocaColaCount variable exists, and, if not, initialize it to 1
        try:
            cocaColaCount += 1     # Check for the cocaColaCount variable, and increment it by one if it exists
        except:
            cocaColaCount = 1      # Create the cocaColaCount variable, which stores the total amount of Coca-Colas the user has ordered
        # Either add Coca-Cola to the dictionary for storing the user's drink orders, or update the total number of Coca-Colas ordered
        drinkOrdersDictionary['Coca-Cola'] = cocaColaCount
        AddSoda.destroy(addSodaClass)       # Remove the window for adding sodas to the order
        SaladOrderingApplication().mainloop()       # Open up the main window again
    def addRootBeer(addSodaClass):
        """Method for adding a root beer to the order. Gives functionality
        to the "Add a root beer" button."""
        # Add the cost of a root beer to the total cost of the order
        global totalPrice
        totalPrice += 1.25
        global rootBeerCount
        # Check to see if the rootBeerCount variable exists, and, if not, initialize it to 1
        try:
            rootBeerCount += 1     # Check for the rootBeerCount variable, and increment it by one if it exists
        except:
            rootBeerCount = 1      # Create the rootBeerCount variable, which stores the total amount of root beers the user has ordered
        # Either add root beer to the dictionary for storing the user's drink orders, or update the total number of root beers ordered
        drinkOrdersDictionary['root beer'] = rootBeerCount
        AddSoda.destroy(addSodaClass)       # Remove the window for adding sodas to the order
        SaladOrderingApplication().mainloop()       # Open up the main window again
    def addSprite(addSodaClass):
        """Method for adding a Sprite to the order. Gives functionality
        to the "Add a Sprite" button."""
        # Add the cost of a Sprite to the total cost of the order
        global totalPrice
        totalPrice += 1.25
        global spriteCount
        # Check to see if the spriteCount variable exists, and, if not, initialize it to 1
        try:
            spriteCount += 1     # Check for the spriteCount variable, and increment it by one if it exists
        except:
            spriteCount = 1      # Create the spriteCount variable, which stores the total amount of Sprites the user has ordered
        # Either add Sprite to the dictionary for storing the user's drink orders, or update the total number of Sprites ordered
        drinkOrdersDictionary['Sprite'] = spriteCount
        AddSoda.destroy(addSodaClass)       # Remove the window for adding sodas to the order
        SaladOrderingApplication().mainloop()       # Open up the main window again
    def addDrPepper(addSodaClass):
        """Method for adding a Dr Pepper to the order. Gives functionality
        to the "Add a Dr Pepper" button."""
        # Add the cost of a Dr Pepper to the total cost of the order
        global totalPrice
        totalPrice += 1.25
        global drPepperCount
        # Check to see if the drPepperCount variable exists, and, if not, initialize it to 1
        try:
            drPepperCount += 1     # Check for the drPepperCount variable, and increment it by one if it exists
        except:
            drPepperCount = 1      # Create the drPepperCount variable, which stores the total amount of Dr Peppers the user has ordered
        # Either add Dr Pepper to the dictionary for storing the user's drink orders, or update the total number of Dr Peppers ordered
        drinkOrdersDictionary['Dr Pepper'] = drPepperCount
        AddSoda.destroy(addSodaClass)       # Remove the window for adding sodas to the order
        SaladOrderingApplication().mainloop()       # Open up the main window again
    def goBack(addSodaClass):
        """Method for returning to the previous window"""
        AddSoda.destroy(addSodaClass)
        AddDrink().mainloop()

class ConfirmationScreen(EasyFrame):
    """Class for creating a confirmation screen that shows what is currently in the order"""
    def __init__(self):
        """Constructor for creating the window and buttons"""
        # Create the window
        EasyFrame.__init__(self, "Review your order")
        # Create a label containing the items currently in the order
        self.addLabel(text = 'Your order: ' + createOrderString(), row = 0, column = 0, columnspan = 3)
        # Create a button to go back
        self.goBack = self.addButton(text = "Go back", row = 1, column = 0, command = self.goBack)
        # Create a button to order for pickup at a store
        self.orderForPickup = self.addButton(text = "Order for pickup", row = 1, column = 1, command = self.orderForPickup)
        # Create a button to have the order delivered
        self.orderForDelivery = self.addButton(text = "Order for delivery", row = 1, column = 2, command = self.orderForDelivery)
    def goBack(self):
        """Method for returning to the previous window"""
        ConfirmationScreen.destroy(self)
        SaladOrderingApplication().mainloop()
    def orderForPickup(self):
        """Method for continuing on to the payment screen (when picking up the order)"""
        ConfirmationScreen.destroy(self)
        OrderForPickup().mainloop()
    def orderForDelivery(self):
        """Method for continuing on to the payment screen (when having the order delivered)"""
        ConfirmationScreen.destroy(self)
        OrderForDelivery().mainloop()

class OrderForPickup(EasyFrame):
    """Class for creating a screen to enter payment details"""
    def __init__(self):
        """Constructor for creating the window and text fields"""
        # Create the window
        EasyFrame.__init__(self, "Enter personal information")
        # Create labels for the text fields
        self.addLabel(text = "Your name:" , row = 0, column = 0)
        self.addLabel(text = "Credit card number:", row = 1, column = 0)
        # Create the text fields
        self.enterName = self.addTextField(text = '', row = 0, column = 1)
        self.enterCreditCard = self.addTextField(text = '', row = 1, column = 1)
        # Create a back button
        self.goBack = self.addButton(text = "Go back", row = 3, column = 0, command = self.goBack)
        # Create a button to confirm the payment details
        self.confirm = self.addButton(text = "Confirm order", row = 3, column = 1, command = self.confirmOrder)
    def goBack(self):
        """Method for returning to the previous window"""
        OrderForPickup.destroy(self)
        ConfirmationScreen().mainloop()
    def confirmOrder(self):
        """Method for confirming payment details are valid and continuing to the "Order successful" screen"""
        # If there is input of any kind in the name box, continue to the next test, otherwise show an error message
        if self.enterName.getText() != '':
            # Try to convert the credit card number to an integer (to confirm that it is solely numbers)
            # If unsuccessful, show an error message
            try:
                int(self.enterCreditCard.getText())
                # If there is something in the credit card number field, continue to the order successful screen
                if self.enterCreditCard.getText() != '':
                    OrderForPickup.destroy(self)
                    OrderSuccessful().mainloop()
            except:
                self.addLabel(text = "Enter a valid credit card number", row = 4, column = 0, columnspan = 2)
        else:
            self.addLabel(text = "Enter a name", row = 5, column = 0)
        
class OrderForDelivery(EasyFrame):
    """Subclass of OrderForPickup that additionally adds a line for entering a delivery location"""
    def __init__(self):
        """Constructor for creating the window and text fields"""
        # Create the window
        EasyFrame.__init__(self, "Enter personal information")
        # Create labels for the text fields
        self.addLabel(text = "Your name:" , row = 0, column = 0)
        self.addLabel(text = "Credit card number:", row = 1, column = 0)
        self.addLabel(text = "Delivery location:", row = 2, column = 0)
        # Create the text fields
        self.enterName = self.addTextField(text = '', row = 0, column = 1)
        self.enterCreditCard = self.addTextField(text = '', row = 1, column = 1)
        self.enterDeliveryLocation = self.addTextField(text = '', row = 2, column = 1)
        # Create a back button
        self.goBack = self.addButton(text = "Go back", row = 3, column = 0, command = self.goBack)
        # Create a button to confirm the payment details
        self.confirm = self.addButton(text = "Confirm order", row = 3, column = 1, command = self.confirmOrder)
    def goBack(self):
        """Method for returning to the previous window"""
        OrderForPickup.destroy(self)
        ConfirmationScreen().mainloop()
    def confirmOrder(self):
        """Method for confirming payment details are valid and continuing to the "Order successful" screen"""
        OrderForPickup.destroy(self)
        OrderSuccessful().mainloop()
    def confirmOrder(self):
        """Method for confirming payment details are valid and continuing to the "Order successful" screen"""
        # If there is input of any kind in the name box, continue to the next test, otherwise show an error message
        if self.enterName.getText() != '':
            # Try to convert the credit card number to an integer (to confirm that it is solely numbers)
            # If unsuccessful, show an error message
            try:
                int(self.enterCreditCard.getText())
                # If there is something in the credit card number field, continue the next test
                if self.enterCreditCard.getText() != '':
                    # If the delivery location text field isn't empty, continue to the order successful screen
                    if self.enterDeliveryLocation.getText() != '':
                        OrderForPickup.destroy(self)
                        OrderSuccessful().mainloop()
                    else:
                        self.addLabel(text = "Enter a delivery location", row = 6, column = 0, columnspan = 2)
            except:
                self.addLabel(text = "Enter a valid credit card number", row = 4, column = 0, columnspan = 2)
        else:
            self.addLabel(text = "Enter a name", row = 5, column = 0)

class OrderSuccessful(EasyFrame):
    """Class for creating a window to inform the user that their order was successful"""
    def __init__(self):
        """Constructor for creating the window and label"""
        # Create the window
        EasyFrame.__init__(self, "Order successful")
        # Create a label informing the user that their order was successful
        self.addLabel(text = "Your order has been placed.", row = 0, column = 0)

def createOrderString():
    """Function for creating a string out of all of the items in a user's order"""
    orderString = ""        # A string for representing the contents of an order
    global totalPrice
    global premadeSaladOrdersDictionary
    global builtSaladsList
    global drinkOrdersDictionary
    if premadeSaladOrdersDictionary != {}:      # If the user has ordered any premade salads, go through the process of adding them to the orderString
        numberOfPremadeSalads = len(premadeSaladOrdersDictionary)       # Get the number of premade salads, to be used in determining when to stop adding to the orderString
        for entry in premadeSaladOrdersDictionary:      # Go through every entry in the dictionary and add it to the orderString
            # Add the number and type of premade salads ordered to the orderString
            orderString += str(premadeSaladOrdersDictionary[entry]) + " "
            orderString += entry
            # Decrement numberOfPremadeSalads by 1
            numberOfPremadeSalads -= 1
            # If there are any premade salads left in the dictionary, add a comma and space to separate them
            if numberOfPremadeSalads > 0:
                orderString += ", "
            # If there are no more premade salads in the list, and either a custom salad or drink was ordered, add a semicolon and space to separate them
            elif numberOfPremadeSalads == 0 and (builtSaladsList != [] or drinkOrdersDictionary != {}):
                orderString += "; "
    if builtSaladsList != []:      # If the user has ordered any custom salads, go through the process of adding them to the orderString
        orderString += "1 salad containing "        # Add an introductory phrase to the orderString
        index = 0       # Create the index variable, used to access the first item in the builtSaladsList
        while True:
            saladIngredientToAdd = builtSaladsList[index]       # Create a variable from the first item in the list to be used to add that ingredient to the custom salad
            builtSaladsList.pop(index)      # Remove the first ingredient from the list
            if saladIngredientToAdd == ';':     # If the first item of the list was a semicolon (which is used to separate different custom salads in an order), continue down this path, otherwise add the ingredient to the orderString
                if builtSaladsList == []:       # If the builtSaladsList is now empty, continue down this path, otherwise add a semicolon to separate custom salads and add another introductory phrase for the next salad
                    # If the user also ordered a drink, add a semicolon to separate the custom salads and the drinks and exit the while loop, otherwise just exit the while loop
                    if drinkOrdersDictionary != {}:
                        orderString += "; "
                        break
                    break
                else:
                    orderString += "; 1 salad containing "
            else:
                orderString += saladIngredientToAdd     # Add the ingredient to the orderString
                saladIngredientToAdd = builtSaladsList[index]       # Determine what the next ingredient in the builtSaladsList is
                # If it isn't a semicolon, and the list isn't empty, add a comma and a space to the orderString (to separate the ingredients in the custom salad)
                if saladIngredientToAdd != ';' and builtSaladsList != []:
                    orderString += ", "
    if drinkOrdersDictionary != {}:      # If the user has ordered any drinks, go through the process of adding them to the orderString
        numberOfDrinks = len(drinkOrdersDictionary)       # Get the number of drinks, to be used in determining when to stop adding to the orderString
        for entry in drinkOrdersDictionary:     # Go through every entry in the dictionary and add it to the orderString
            # Add the number and type of drinks ordered to the orderString
            orderString += str(drinkOrdersDictionary[entry]) + " "
            orderString += entry
            # Decrement numberOfDrinks by 1
            numberOfDrinks -= 1
            # If there are any drinks left in the dictionary, add a comma and space to separate them, otherwise don't add anything
            if numberOfDrinks > 0:
                orderString += ", "
    # Add the total price of the order to the orderString
    orderString += ". Total price: $" + str(totalPrice)
    return orderString

def main():     # Open up the GUI for the application
    SaladOrderingApplication().mainloop()

if __name__ == '__main__':
    main()      # Call on the main() function
