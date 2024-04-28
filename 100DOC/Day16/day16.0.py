# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# #object methods
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)
#
# my_screen = Screen()
# print(type(my_screen))
# # object attributes
# print(my_screen.canvheight)
# print(my_screen.canvwidth)
# # object method
# my_screen.exitonclick()





from prettytable import PrettyTable

table = PrettyTable()
table.add_column('Pokimon Name', ['Pikachu', 'Squirtle', 'Charmander'])
table.add_column('Type', ['Electric', 'water', 'fire'])
table.align = 'l'
print(table)
