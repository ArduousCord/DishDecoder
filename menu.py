# Define a dictionary with menu items and their ingredients
menu_items = {
    \
Spaghetti
Bolognese\: [\spaghetti\, \ground
beef\, \tomato
sauce\, \onion\, \garlic\, \olive
oil\, \salt\, \pepper\],
    \Caesar
Salad\: [\romaine
lettuce\, \croutons\, \parmesan
cheese\, \Caesar
dressing\, \chicken
breast\, \salt\, \pepper\],
    \Margherita
Pizza\: [\pizza
dough\, \tomato
sauce\, \mozzarella
cheese\, \basil\, \olive
oil\, \salt\],
    \Chicken
Curry\: [\chicken
breast\, \curry
powder\, \coconut
milk\, \onion\, \garlic\, \ginger\, \salt\, \pepper\]
}

# Function to get ingredients for a given menu item
def get_ingredients(menu_item):
    return menu_items.get(menu_item, \Menu
item
not
found\)

# Example usage
menu_item = input(\Enter
a
menu
item:
\)
ingredients = get_ingredients(menu_item)
print(f\Ingredients
for
menu_item
:
ingredients
\)
