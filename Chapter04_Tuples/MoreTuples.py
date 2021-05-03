# Exemplo de criação de tuplas.
emptyTuple = () # Também é possível fazer: tupla_vazia = tuple()
print("Tupla vazia: ", emptyTuple)

coordinate_xy = (10, 20)
print("Exemplo de tupla: ", coordinate_xy)
print("Tipo de uma tupla: ", type(coordinate_xy))

place = (-19.8157, -43.9542)
print("Outro exemplo de criação de tupla: ", place)

# Extraindo elementos de uma tupla
x, y = coordinate_xy
print("x =", x)
print("y =", y)

# Tuples can not be modified
# coordinate_xy[0] = 15
