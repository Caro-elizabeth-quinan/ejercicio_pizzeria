#ejercicio sistema de pedidos 
import os,time
os.system("cls")
pedidos=[]
pizzas=[]
while True:
        print("=== PIZZERÍA LA MÁS RICA ===")
        print("1. Registrar nueva pizza")
        print("2. Ver catálogo de pizzas")
        print("3. Realizar pedido")
        print("4. Ver pedidos realizados")
        print("5. Salir")
        opcion=input("selecciones una opción (1-5):") 
        if opcion=="1":
                codigo = int(input("Ingrese código único de la pizza: "))
                nombre = input("Ingrese nombre de la pizza: ").strip().title()
                masa = input("Ingrese tipo de masa: ").strip().title()
                precio = float(input("Ingrese precio unitario: $"))
                stock = int(input("Ingrese stock disponible: "))

                pizza = {
              "codigo": codigo,
              "nombre": nombre,
              "masa": masa,
             "precio": precio,
             "stock": stock
              }
                pizzas.append(pizza)
                print("Pizza registrada correctamente.")
                time.sleep(2)
        elif opcion=="2":
                if len(pizzas) == 0:
                   print("No hay pizzas registradas.")
                else:
                   print("\n--- CATÁLOGO DE PIZZAS ---")
        
        elif opcion=="3":
                pass
        elif opcion=="4":
                pass
        elif opcion=="5":
                print("saliendo...")
        else:
                print("la opción no es correcta.intentalo de nuevo.")
        input("presiona una tecla para continuar....")