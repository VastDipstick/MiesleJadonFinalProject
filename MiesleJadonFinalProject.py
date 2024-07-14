"""

Jadon Miesle
7/13/24
Final Project


"""

"""
Known issues/To do:
    window name doesn't update upon closing a window
    Back buttons
    Images
    Add a short description for each item (probably just for the premade salads and salad ingredients)
    Devise a system for storing the user's choices for the premade salads
    Add a confirmation screen upon clicking the checkout button
    Activate the checkout button after adding any item
    Documentation
"""

from breezypythongui import EasyFrame

global totalPrice
totalPrice = 0.00
global drinkOrdersDictionary     # Dictionary used for storing the types and quantities of drinks ordered
drinkOrdersDictionary = {}

class saladOrderingApplication(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, 'Salad Ordering Application')
        self.addSaladButton = self.addButton(text = 'Add a salad', row = 0, column = 0, command = self.addSalad)
        self.addADrinkButton = self.addButton(text = 'Add a drink', row = 1, column = 0, command = self.addADrink)
        self.checkoutButton = self.addButton(text = 'Proceed to checkout', row = 2, column = 0, command = self.proceedToCheckout, state = 'disabled')
    def addSalad(self):
        None
    def addADrink(self):
        addDrink().mainloop()
    def proceedToCheckout(self):
        None

class addDrink(EasyFrame):
    def __init__(addDrinkClass):
        EasyFrame.__init__(addDrinkClass, 'Add a drink')
        addDrinkClass.addWaterButton = addDrinkClass.addButton(text = 'Add a bottled water: + $0.75', row = 0, column = 0, command = addDrinkClass.addWater)
        addDrinkClass.addLemonadeButton = addDrinkClass.addButton(text = 'Add a lemonade:  + $1.25', row = 1, column = 0, command = addDrinkClass.addLemonade)
        addDrinkClass.addPinkLemonadeButton = addDrinkClass.addButton(text = 'Add a pink lemonade: + $1.25', row = 2, column = 0, command = addDrinkClass.addPinkLemonade)
        addDrinkClass.addSodaButton = addDrinkClass.addButton(text = 'Add a soda: + $1.25', row = 3, column = 0, command = addDrinkClass.addSoda)
    def addWater(addDrinkClass):
        global totalPrice
        totalPrice += 0.75
        global waterCount
        try:
            waterCount += 0
        except:
            waterCount = 0
        waterCount += 1
        drinkOrdersDictionary['water'] = waterCount
        addDrink.destroy(addDrinkClass)     # Doesn't update window name; needs fixed
    def addLemonade(addDrinkClass):
        global totalPrice
        totalPrice += 1.25
        global lemonadeCount
        try:
            lemonadeCount += 0
        except:
            lemonadeCount = 0
        lemonadeCount += 1
        drinkOrdersDictionary['lemonade'] = lemonadeCount
        addDrink.destroy(addDrinkClass)     # Doesn't update window name; needs fixed
    def addPinkLemonade(addDrinkClass):
        global totalPrice
        totalPrice += 1.25
        global pinkLemonadeCount
        try:
            pinkLemonadeCount += 0
        except:
            pinkLemonadeCount = 0
        pinkLemonadeCount += 1
        drinkOrdersDictionary['pink lemonade'] = pinkLemonadeCount
        addDrink.destroy(addDrinkClass)     # Doesn't update window name; needs fixed
    def addSoda(addDrinkClass):
        addDrink.destroy(addDrinkClass)
        addSoda().mainloop()
        

class addSoda(EasyFrame):
    def __init__(addSodaClass):
        EasyFrame.__init__(addSodaClass, 'Add a soda')
        addSodaClass.addPepsiButton = addSodaClass.addButton(text = 'Add a Pepsi', row = 0, column = 0, command = addSodaClass.addPepsi)
        addSodaClass.addCocaColaButton = addSodaClass.addButton(text = 'Add a Coca-Cola', row = 1, column = 0, command = addSodaClass.addCocaCola)
        addSodaClass.addRootBeerButton = addSodaClass.addButton(text = 'Add a Root Beer', row = 2, column = 0, command = addSodaClass.addRootBeer)
        addSodaClass.addSpriteButton = addSodaClass.addButton(text = 'Add a Sprite', row = 3, column = 0, command = addSodaClass.addSprite)
        addSodaClass.addDrPepperButton = addSodaClass.addButton(text = 'Add a Dr Pepper', row = 4, column = 0, command = addSodaClass.addDrPepper)
    def addPepsi(addSodaClass):
        global totalPrice
        totalPrice += 1.25
        global pepsiCount
        try:
            pepsiCount += 0
        except:
            pepsiCount = 0
        pepsiCount += 1
        drinkOrdersDictionary['Pepsi'] = pepsiCount
        addSoda.destroy(addSodaClass)
    def addCocaCola(addSodaClass):
        global totalPrice
        totalPrice += 1.25
        global cocaColaCount
        try:
            cocaColaCount += 0
        except:
            cocaColaCount = 0
        cocaColaCount += 1
        drinkOrdersDictionary['Coca Cola'] = cocaColaCount
        addSoda.destroy(addSodaClass)
    def addRootBeer(addSodaClass):
        global totalPrice
        totalPrice += 1.25
        global rootBeerCount
        try:
            rootBeerCount += 0
        except:
            rootBeerCount = 0
        rootBeerCount += 1
        drinkOrdersDictionary['root beer'] = rootBeerCount
        addSoda.destroy(addSodaClass)
    def addSprite(addSodaClass):
        global totalPrice
        totalPrice += 1.25
        global spriteCount
        try:
            spriteCount += 0
        except:
            spriteCount = 0
        spriteCount += 1
        drinkOrdersDictionary['Sprite'] = spriteCount
        addSoda.destroy(addSodaClass)
    def addDrPepper(addSodaClass):
        global totalPrice
        totalPrice += 1.25
        global drPepperCount
        try:
            drPepperCount += 0
        except:
            drPepperCount = 0
        drPepperCount += 1
        drinkOrdersDictionary['Dr Pepper'] = drPepperCount
        addSoda.destroy(addSodaClass)

        


def main():     # Open up the GUI for the application
    saladOrderingApplication().mainloop()

if __name__ == '__main__':
    main()      # Call on the main() function
    print(drinkOrdersDictionary)