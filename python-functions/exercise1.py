# > Etapa 1

# def say_hello():
#     print('Hello World!')

# say_hello()

# > Etapa 2

# def say_hello(name):
#     print(f'Hello {name}!')

# say_hello('Alan')

# > Etapa 3

# def say_hello(name='World'):
#     print(f'Hello {name}!')

# say_hello()
# say_hello('Alan')

# > Etapa 4

# def say_hello(name='World', greeting=None):
#     if greeting == None:
#         print(f'Hello {name}!')
#     else:
#         print(f'{greeting} {name}!')

# say_hello()
# say_hello('Alan')
# say_hello(greeting='Howdy')
# say_hello('Alan', "Howdy")

# print(type(None))

# > Etapa 5

# def add_two_numbers(x, y):
#     return x + y

# add_two_numbers(4, 6)
# result = add_two_numbers(5, 7)
# print(result)

# > Etapa 6

# def create_deck():
#     suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
#     ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
#     deck = []

#     for suit in suits:
#         for rank in ranks:
#             deck.append(f'{rank} of {suit}')
    
#    return deck

# my_deck = create_deck()
# print(len(my_deck))

# > Etapa 7

value = 1

def some_function():
    value = 10
    return value

print(value)
some_function()
print(value)