# Scope

# enemies = 1

# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

# Local Scope

# def drink_potion():
#   potion_strenght = 2
#   print(potion_strenght)

# drink_potion()
# print(potion_stength)

# Global Scope

# player_health = 10

# def game():  # drink_potion() has local scope within the game() function now.
#     def drink_potion():
#         potion_stength = 2
#         print(player_health)

#     drink_potion() - Will print NameError if not nested in drink_potion().
# print(player_health)


# There is no Block Scope in Python!

# if 3 > 2:
#     a_variable = 10 # Still has global scope.and

# game_level = 3
# enemies = ['Skeleton', 'Zombie', 'Alien']


# if game_level < 5:
#   new_enemy = enemies[0]

# print(new_enemy) # No error

# Nesting conditional within a function.

# def create_enemy():
#   if game_level < 5:
#   new_enemy = enemies[0] # Local scope.

# print(new_enemy) # NameError

# Modifying Global Scope

enemies = 1


def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1


increase_enemies()
print(f"enemies outside function: {enemies}")


# Global Constants

PI = 3.14159  # Use uppercase to show that these are global constants.
