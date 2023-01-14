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
