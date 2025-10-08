# En Python, un set (conjunto) es una colección de elementos únicos, es decir, no se repiten y no tienen un orden específico.
# Unos corchetes vacíos {} siempre crean un diccionario, no un set.

my_set = set()
print(my_set)
my_other_set = {"bear", "elliot"}
print("tipo de dato: ", type(my_other_set))

primer = {1, 2, 2, 1, 3, 4}
segundo = [3, 4, 5, 6, 7]
segundo = set(segundo)
print(primer ^ segundo)

frutas = {"manzana", "pera", "uva"}
otras = {"pera", "mango", "kiwi"}

print(frutas | otras)   # Unión
print(frutas & otras)   # Intersección
print(frutas - otras)   # Diferencia

print(frutas.add("banana"))
print(frutas.add("tamarindo"))
print("Longitud de frutas: ", len(frutas))
print("manzana" in frutas)
# Se pueden realizar busquedas

a = {"rojo", "azul", "verde"}
b = {"amarillo", "azul", "negro"}

resultado = a.union(b)

print(resultado)
