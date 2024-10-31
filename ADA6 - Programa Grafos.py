import networkx as nx
import matplotlib.pyplot as plt
from itertools import permutations, product

# Definición de los estados y las relaciones
estados = {
    'Chiapas': {'Tabasco': 50, 'Guerrero': 100},
    'Tabasco': {'Veracruz': 70, 'Chiapas': 50, 'Campeche': 60},
    'Veracruz': {'Puebla': 80, 'Tabasco': 70},
    'Puebla': {'Tlaxcala': 30, 'Veracruz': 80, 'Hidalgo': 90},
    'Hidalgo': {'Tlaxcala': 40, 'Puebla': 90},
    'Guerrero': {'Oaxaca': 120, 'Chiapas': 100},
    'Oaxaca': {'Guerrero': 120}
}

G = nx.Graph()
# Agregar nodos y aristas al grafo
for estado, conexiones in estados.items():
    for vecino, costo in conexiones.items():
        G.add_edge(estado, vecino, weight=costo)

def costo_recorrido(recorrido):
    costo_total = 0
    for i in range(len(recorrido) - 1):
        if G.has_edge(recorrido[i], recorrido[i + 1]):
            costo_total += G[recorrido[i]][recorrido[i + 1]]['weight']
        else:
            return None  # Retornar None si no hay conexión
    return costo_total

def sin_repetir():
    total_costs = []
    print("\nRecorridos sin repetir:")
    for recorrido in permutations(estados.keys()):
        costo = costo_recorrido(recorrido)
        if costo is not None:  # Solo imprimir recorridos válidos
            total_costs.append(costo)
            print(f"Recorrido: {' -> '.join(recorrido)} | Costo Total: {costo}")
    print(f"\nEl costo total de recorridos sin repetir es de: {sum(total_costs) if total_costs else 'No hay recorridos válidos'}")

def con_repeticion():
    estados_lista = list(estados.keys())
    total_costs = []
    print("\nRecorridos con repetición de al menos un estado:")

    for recorrido in product(estados_lista, repeat=8):
        if len(set(recorrido)) >= 7: 
            costo = costo_recorrido(recorrido)
            if costo is not None:  
                total_costs.append(costo)
                print(f"Recorrido: {' -> '.join(recorrido)} | Costo Total: {costo}")
    print(f"\nEl costo total de recorridos con repetición es de: {sum(total_costs) if total_costs else 'No hay recorridos válidos'}")

def grafo():
    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title('Grafo de Estados de México')
    plt.show()

def menu():
    while True:
        print("\nMenú de opciones disponibles:")
        print("1. Recorrer todos los estados sin repetir ninguno")
        print("2. Recorrer todos los estados repitiendo al menos uno de ellos")
        print("3. Dibujar el grafo")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            sin_repetir()
        elif opcion == '2':
            con_repeticion()
        elif opcion == '3':
            grafo()
        elif opcion == '4':
            print("\nSaliendo del programa....\n")
            break
        else:
            print("Opción inválida, intenta de nuevo.")

menu()
