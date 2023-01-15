# Python OOP Challenge 2:

# 1.) Create a class named Menu. The class should have 4 parameters (name, items, start_time and end_time).

# 2.) Create 4 menus with the name and timing of: Brunch (11-16), Early Bird (15-18), Dinner (17-23), Kids (11-21) by using the 4 dictionaries provided below:

# 3.) Create a string representation method for the class Menu and test it. It should indicate the menu's name and time.

# 4.) Create a .calculate_bill() method with the parameter purchased_items. The method should return the total price of purchases consisting of all items in purchased_items.

# 5.) Test out the .calculate_bill() method with a brunch order of one pancake, one home fries & one coffee. Print out the result.

# 6.) Test out the .calculate_bill() method with a early bird order of one salumeria plate & one vegan mushroom ravioli. Print out the result.

# 7.) Create a second class named Franchise. The class should have 2 parameters (address and menus)

# 8.) Create two objects, flagship_store and new_installment with the address "1232 West End Road" and "12 East Mulberry Street" respectively.

# 9.) Create a string representation method for the class Franchise and test it. It should indicate the franchise's address.

# 10.) Create a method for Franchise called .available_menus(), taking the parameter "time" and returning a list of the Menu objects that are available at that time.

# 11.) Test out the .available_menus() method with 12 noon as an argument, and print out the result.

# 12.) Test out the .available_menus() method with 5 pm as an argument, and print out the result.

# 13.) Create a class named Business. The class should have 2 parameters (name and a list, franchises).

# 14.) Create the first object called Business with the name "Basta Fazoolin' with my Heart", and the list containing flagship_store and new_installment.

# 15.) Create a new menu variable named arepas_menu, with the following keys & values: {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}.

# 16.) Create a new franchise with an address of "189 Fitzgerald Avenue". Save the franchise to a variable called arepas_place.

# 17.) Create a new business called "Take a' Arepa". Repeat the process as required.

brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 
  'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 
  'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
  }

early_bird_items = {
  'salumeria plate': 8.00, 
  'salad and breadsticks (serves 2, no refills)': 14.00, 
  'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 
  'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 
  'espresso': 3.00
  }

dinner_items = {
  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.0,
  'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 
  'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00
  }

kids_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 
  'apple juice': 3.00
  }

# Start writing your code below -------------------------------------------------------

class Menu:

  def __init__(self,name,items,start_time,end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    return "{name} menu available from {start_time} to {end_time}".format(name = self.name, start_time = self.start_time, end_time = self.end_time)

  def calculate_bill(self, purchased_items):
    total_price = 0
    # Purchased items being the array (['pancakes', 'home fries', 'coffee']).
    # item being pancakes.
    # self.items resembling @items in Ruby which is a hash.
    # self.items[item] resembling @items[pancakes].
    for item in purchased_items:
      if item in self.items:
        total_price += self.items[item]
    return total_price

class Franchise:
  def __init__(self,address,menus):
    self.address = address
    self.menus = menus
  
  def __repr__(self):
    return "{} is this franchise's address.".format(self.address)
  
  def available_menus(self,time):
    available_menu = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available_menu.append(menu)
    return available_menu

# Menu & Franchise Variables:

brunch_menu = Menu('Brunch', brunch_items, 11, 16)

early_bird_menu = Menu('Early Bird', early_bird_items, 15, 18)

dinner_menu = Menu('Dinner', dinner_items, 17, 23)

kids_menu = Menu('Kids', kids_items, 11, 21)

menus = [brunch_menu, early_bird_menu, dinner_menu , kids_menu]

flagship_store = Franchise("1232 West End Road", menus)

new_installment = Franchise("12 East Mulberry Street", menus)


first_order = ['pancakes', 'home fries', 'coffee']
second_order = ['salumeria plate', 'vegan mushroom ravioli']


# Code testing:
print(brunch_menu)
print(early_bird_menu)
print(dinner_menu)
print(kids_menu)
print("")
 
print(brunch_menu.calculate_bill(first_order))
print(early_bird_menu.calculate_bill(second_order))
print("")

print(flagship_store)
print("")

print(flagship_store.available_menus(12))
print(flagship_store.available_menus(17))
print("")
