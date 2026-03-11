#---------------------------------
#SOLICITA EL NOMBRE DEL PRODUCTO
#---------------------------------
nombre_valido = False
while nombre_valido == False:
    nombre = input("Ingrense el nombre de producto: ")
    if nombre.split() == "":
        print("Error el nombre no puede estar vacio")
    else:
        nombre_valido = True
#---------------------------------
#SOLICITA EL PRECIO DEL PRODUCTO
#---------------------------------
precio_valido = False
while precio_valido == False:
    precio = input("Ingresa el precio: ")
    try:
        precio = float(precio)
        precio_valido = True
    except:
        print("Error, ingrese un numero valido")
#-----------------------------------
#SOLICITA LA CANTIDAD DEL PRODUCTO
#-----------------------------------
cantidad_valida = False
while cantidad_valida == False:
    cantidad = input("Ingrese la cantidad: ")
    try:
        cantidad = int(cantidad)
        cantidad_valida =True
    except:
        print("Error, ingrese un numero entero valido")
#-------------------------------------------------------------------
#MULTIPLICA EL PRECIO X CANTIDAD PARA DAR EL COSTO TOTAL CALCULADO
#-------------------------------------------------------------------
precio_total = precio * cantidad
#------------------------------------------------------------------------
#MUESTRA LOS DATOS INGRESADOS POR EL USUARIO Y EL COSTO TOTAL CALCULADO
#------------------------------------------------------------------------
print("-------------------------------")
print("      DATOS GUARDADOS")
print("-------------------------------")
print(f"|  Nombre de producto: {nombre}")
print(f"|  Precio unitario: {precio}")
print(f"|  Cantidad: {cantidad}")
print(f"|  Costo total calculado: {precio_total}")
print("-------------------------------")
