# The order in which you store the data matters and will be kept.

states_of_america = [
                    "Delaware", "Pennsylvania", "New Jersey", "Georgia",
                    "Connecticut", "Massachusetts", "Maryland",
                    "South Carolina", "New Hampshire", "Virginia", "New York",
                    "North Carolina", "Rhode Island", "Vermont", "Kentucky",
                    "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi",
                    "Illinois", "Alabama", "Maine", "Missouri", "Arkansas",
                    "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
                    "California", "Minnesota", "Oregon", "Kansas",
                    "West Virginia", "Nevada", "Nebraska", "Colorado",
                    "North Dakota", "South Dakota", "Montana", "Washington",
                    "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico",
                    "Arizona", "Alaska", "Hawaii"
                    ]
num_of_states = len(states_of_america)

print(states_of_america[0])

# See [], relate it to list!
# Adding info to list - append will add a single item to the end of the list.
states_of_america.append('Connecticut')
print(states_of_america[4])

# Extend - adds a bunch of items to the list.
states_of_america.extend(['Massachussets', 'Maryland', 'South Carolina'])
print(states_of_america)

# Nested lists.
fruits = [
          "Strawberries", "Nectarines", "Apples", "Grapes",
          "Peaches", "Cherries", "Pears"
         ]

vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen)

print(dirty_dozen[1][1])
