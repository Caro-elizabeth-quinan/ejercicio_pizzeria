#ejercicio sistema de pedidos 
import os
import time

os.system("cls")

pedidos = []
pizzas = []

while True:
    print("=== PIZZERÍA LA MÁS RICA ===")
    print("1. Registrar nueva pizza")
    print("2. Ver catálogo de pizzas")
    print("3. Realizar pedido")
    print("4. Ver pedidos realizados")
    print("5. Salir")
    opcion = input("Seleccione una opción (1-5): ").strip()

    if opcion == "1":
        while True:
            try:
                codigo = int(input("Ingrese código único de la pizza: "))
                # Verifique que el código no este repetido
                if any(p["codigo"] == codigo for p in pizzas):
                    print("Error: El código ya existe. Intente otro.")
                break
            except ValueError:
                print("debes ingresar un número válido.")

        while True:
            nombre = input("Ingrese nombre de la pizza: ").strip()
            if nombre != "": #verifique que el nombre no este vacío
                nombre = nombre.title()
                break
            print("El nombre no puede estar vacío.")

        while True:
            masa = input("Ingrese tipo de masa: ").strip()
            if masa != "":
                masa = masa.title()
                break
            print("El tipo de masa no puede estar vacío.")

        while True:
            try:
                precio = float(input("Ingrese el precio : $"))
                if precio > 0:
                    break
                else:
                    print("El precio debe ser mayor a 0.")
            except ValueError:
                print("debes ingresar un número válido.")

        while True:
            try:
                stock = int(input("Ingrese stock disponible: "))
                if stock >= 0:
                    break
                else:
                    print("El stock no puede ser negativo.")
            except ValueError:
                print("Debes ingresar un número válido.")

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

    elif opcion == "2":
        if len(pizzas) == 0:
            print("No hay pizzas registradas.")
        else:
            print("\n--- Catálogo de pizzas ---")
            for p in pizzas:
                print(f"Código: {p['codigo']}, Nombre: {p['nombre']}, Masa: {p['masa']}, Precio: ${p['precio']:.2f}, Stock: {p['stock']}")
        input("\nPresione Enter para continuar...")

    elif opcion == "3":
        if len(pizzas) == 0:
            print("No hay pizzas disponibles para pedir.")
            time.sleep(2)

        # Valide que el nombre no este vacío de la misma forma de la anterior 
        while True:
            cliente = input("Ingrese nombre del cliente: ").strip()
            if cliente != "":
                cliente = cliente.title()
                break
            else:
                print("El nombre del cliente no puede estar vacío. Inténtalo de nuevo.")

        print("\n--- PIZZAS DISPONIBLES ---")
        for p in pizzas:
            print(f"Código: {p['codigo']}, Nombre: {p['nombre']}, Precio: ${p['precio']:.2f}, Stock: {p['stock']}")

        while True:
            try:
                codigo_pedido = int(input("Ingrese código de la pizza a pedir: "))
                break
            except ValueError:
                print("Debe ingresar un número válido para el código.")

        encontrado = False
        pizza_seleccionada =None

        for p in pizzas:
            if p["codigo"] == codigo_pedido:
                pizza_seleccionada = p
                encontrado = True
                break

        if not encontrado:
            print("No se encontró la pizza con ese código.")
            time.sleep(2)

        if pizza_seleccionada["stock"] == 0:
            print("No hay stock disponible de esta pizza.")
            time.sleep(2)

        while True:
            try:
                cantidad = int(input("Ingrese cantidad a pedir: "))
                if cantidad > 0:
                    if cantidad <= pizza_seleccionada["stock"]:
                        break
                    else:
                        print(f"Stock insuficiente. Solo hay {pizza_seleccionada['stock']} disponibles.")
                else:
                    print("La cantidad debe ser mayor a cero.")
            except ValueError:
                print("Debe ingresar un número válido para la cantidad.")

        total = pizza_seleccionada["precio"] * cantidad
        pizza_seleccionada["stock"] -= cantidad

        pedido = {
            "cliente": cliente,
            "pizza": pizza_seleccionada["nombre"],
            "cantidad": cantidad,
            "total": total
        }
        pedidos.append(pedido)

        print(f"Pedido realizado. Total a pagar: ${total:.2f}")
        time.sleep(3)

    elif opcion == "4":
        if len(pedidos) == 0:
            print("No se han realizado pedidos aún.")
        else:
            print("\n--- Pedidos realizados ---")
            i = 1
            for ped in pedidos:
                print(f"{i}. Cliente: {ped['cliente']}, Pizza: {ped['pizza']}, Cantidad: {ped['cantidad']}, Total: ${ped['total']:.2f}")
                i += 1
        input("\nPresione Enter para continuar...")

    elif opcion == "5":
        print("Saliendo...")
        time.sleep(1)
        break

    else:
        print("La opción no es correcta. Inténtalo de nuevo.")
        time.sleep(2)