#Saludo de bienvenida
print("*****Saludos señor usuario******")
print("****Bienvenido****")
print("***a la Panadería***")
print("**La Mañanera**")

# Opción de mejora en esta parte haciendo que el sistema solo pueda recibir letras en el input para generar un nombre válido
nombre=(input("Por favor ingresa tu nombre "))
apellido=(input("Por favor ingresa tu apellido "))

nombre_completo=nombre+" "+apellido

print("Gracias por visitarnos,",nombre_completo)

num_pandequesos = 51
num_buñuelos = 63
num_panes_integrales = 28

# defininiendo funciones
def mostrar_menu():
    print("\nSelecciona la opción que deseas")
    print("1: Conocer cuantos productos tiene la panadería")
    print("2: Comprar un producto en especial")
    print("3: Salir")

def mostrar_inventario():
    print("\nActualmente contamos con:")
    print("Pandequesos:",num_pandequesos," Buñuelos:", num_buñuelos, "Panes integrales:",num_panes_integrales)
# def funcionan de compra y if anidados para validar disponibilidad de producto   
def comprar_producto():
    print("\nQue producto deseas comprar:")
    print("Opción 1: Pandequesos")
    print("Opción 2: Buñuelos")
    print("Opción 3: Panes integrales")
    producto= int(input())
    cantidad = int(input("Cuantas unidades deseas "))
    num_pandequesos = 51
    num_buñuelos = 63
    num_panes_integrales = 28
    if producto == 1:
        producto = "pandequesos"
        if cantidad <= num_pandequesos:
            num_pandequesos -= cantidad
            print("Has comprado ",cantidad, producto, "en total")
        else:
            print("No hay suficientes pandequesos disponibles, ingresa un valor válido")
    elif producto == 2:
        producto = "buñuelos"
        if cantidad <= num_buñuelos:
            num_buñuelos -= cantidad
            print("Has comprado ",cantidad, producto, "en total")
        else:
            print("No hay suficientes buñuelos disponibles, ingresa un valor válido")
    elif producto == 3:
        producto = "panes integrales"
        if cantidad <= num_panes_integrales:
            num_panes_integrales -= cantidad
            print("Has comprado ",cantidad, producto, "en total")
        else:
            print("No hay suficientes panes integrales disponibles, ingresa un valor válido")
    else:
        print("Ingresa una opción válida")
     
# Opcion de mejora en la función de comprar productos utilizando un contador para reducir la cantidad de productos en el inventario   
# ciclo para utilizar las funciones creadas
while True:
    mostrar_menu()
    respuesta = int(input())

    if respuesta == 1:
        mostrar_inventario()
    elif respuesta == 2:
        comprar_producto()
    elif respuesta == 3: 
        print("Has terminado tu compra, vuelve pronto")
        break
    else:
        print("Por favor ingresa una opción válida")
        
print("Terminando programa")


